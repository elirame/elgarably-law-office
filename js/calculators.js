/*
   ==========================================================================
   Adv. Eliram Elgarably - Real Estate Law Firm
   Transaction Cost Calculators - Shared Engine
   --------------------------------------------------------------------------
   Powers two standalone calculator pages:
     - calculators/buy-second-hand/       (resale apartment)
     - calculators/buy-from-contractor/   (new build from a developer)

   SINGLE SOURCE OF TRUTH:
   The purchase-tax math (brackets, disabled/immigrant logic) is NOT duplicated
   here. It is consumed from js/main.js, which must load BEFORE this file:
       TAX_BRACKETS, computeTaxBreakdown(price, type, gift)  -> { total, rows }
       currentLanguage, currentDisabledSubType                (shared state)
   All other figures (VAT, contractor lawyer-fee cap, registry fees) are defined
   once below and verified for 2026.
   ==========================================================================
*/

/* ----- Verified 2026 constants (single definition, shared by both pages) ----- */
const CALC_VAT_RATE = 0.18;                         // 18% VAT (since 1.1.2025)
const CONTRACTOR_LAWYER_CAP = 5915;                 // ₪, excl. VAT — Sale Law expense-limit regs (2026)
const CONTRACTOR_LAWYER_CEILING_PRICE = 4642750;    // ₪ — price ceiling above which the statutory cap does not apply
const GOV_FEE = {                                   // Land Registry (Tabu) fees, ₪ — editable defaults, verify vs. official tariff
  tabu: 18, joint: 39, warnBuyer: 150, warnBank: 150, mortgage: 188, ownership: 44, tabuAfter: 18
};

/* Per-page UI state */
const calcFeeModes = { sh: { brokerage: 'percent', lawyer: 'percent' }, c: { lawyerBuyer: 'percent' } };
const calcFixedFees = { sh: { brokerage: 0, lawyer: 0 }, c: { lawyerBuyer: 0 } };
let calcBuyerType = { sh: 'single', c: 'single' };
let calcFeesCustom = false;       // contractor: user overrode the registry-fee estimate
let calcLastReport = null;        // snapshot of the latest calculation, used by the branded report

/* ----- Small i18n helpers (language comes from main.js global currentLanguage) ----- */
function calcIsHe() { return (typeof currentLanguage !== 'undefined' ? currentLanguage : 'he') === 'he'; }
function calcParse(str) { return parseInt(String(str == null ? '' : str).replace(/\D/g, ''), 10) || 0; }
function calcFmt(n) { return Math.round(n).toLocaleString(calcIsHe() ? 'he-IL' : 'en-US'); }
function calcCur(n) { return calcIsHe() ? (calcFmt(n) + ' ₪') : ('₪ ' + calcFmt(n)); }
function calcT(he, en) { return calcIsHe() ? he : en; }

/* ==========================================================================
   Boot
   ========================================================================== */
document.addEventListener('DOMContentLoaded', function () {
  if (document.getElementById('price-sh')) {
    restoreSecondHandFromUrl();
    initChartTooltips('sh');
    initCalcTipTaps();
    setBuyerType('sh', calcBuyerType.sh);
    onSliderChange('sh');
    calculate();
  } else if (document.getElementById('price-c')) {
    restoreContractorFromUrl();
    initChartTooltips('c');
    initCalcTipTaps();
    setBuyerType('c', calcBuyerType.c);
    onSliderChange('c');
    calculate();
  }
});

/* Re-render dynamic (JS-generated) text when the language switch is used.
   main.js setLanguage() calls window.renderActiveCalculator() if present. */
function renderActiveCalculator() {
  if (document.getElementById('price-sh') || document.getElementById('price-c')) calculate();
}

/* ==========================================================================
   Shared input helpers (names match inline handlers in the markup)
   ========================================================================== */
function calculate() {
  if (document.getElementById('price-sh')) recalcSecondHand();
  else if (document.getElementById('price-c')) recalcContractor();
}

function formatAndCalculate() {
  const isSH = !!document.getElementById('price-sh');
  const priceId = isSH ? 'price-sh' : 'price-c';
  const priceEl = document.getElementById(priceId);
  if (priceEl) { const v = calcParse(priceEl.value); priceEl.value = v > 0 ? v.toLocaleString('he-IL') : ''; }

  ['renovation-sh', 'upgrades-c', 'mortgage-val-sh', 'mortgage-val-c', 'appraisal-val-sh', 'appraisal-val-c']
    .forEach(function (id) {
      const el = document.getElementById(id);
      if (!el) return;
      const v = calcParse(el.value);
      const zeroable = (id.indexOf('renovation') === 0 || id.indexOf('upgrades') === 0);
      el.value = v > 0 ? v.toLocaleString('he-IL') : (zeroable ? '0' : '');
    });

  if (!isSH && !calcFeesCustom) {
    const price = calcParse((document.getElementById('price-c') || {}).value);
    const auto = Math.round(price * 0.0025);
    const feesEl = document.getElementById('fees-c');
    if (feesEl) feesEl.value = auto > 0 ? auto.toLocaleString('he-IL') : '0';
  }
  calculate();
}

function setBuyerType(scope, value) {
  calcBuyerType[scope] = value;
  document.querySelectorAll('[id^="rc-' + scope + '-"]').forEach(function (el) { el.classList.remove('active'); });
  const card = document.getElementById('rc-' + scope + '-' + value);
  if (card) {
    card.classList.add('active');
    const radio = card.querySelector('input[type="radio"]');
    if (radio) radio.checked = true;
  }
  // The disabled/blind track defaults to single-home logic (Regulation 11).
  if (value === 'disabled' && typeof currentDisabledSubType !== 'undefined') currentDisabledSubType = 'single';
  calculate();
}

function onSliderChange(scope) {
  if (scope === 'sh') {
    if (calcFeeModes.sh.brokerage === 'percent') {
      const v = parseFloat(document.getElementById('rate-brokerage-sh').value).toFixed(1);
      document.getElementById('val-brokerage-sh').value = v + '%';
    }
    if (calcFeeModes.sh.lawyer === 'percent') {
      const v = parseFloat(document.getElementById('rate-lawyer-sh').value).toFixed(1);
      document.getElementById('val-lawyer-sh').value = v + '%';
    }
  } else if (scope === 'c') {
    if (calcFeeModes.c.lawyerBuyer === 'percent') {
      const v = parseFloat(document.getElementById('rate-lawyer-buyer-c').value).toFixed(1);
      document.getElementById('val-lawyer-buyer-c').value = v + '%';
    }
  }
  calculate();
}

function setFeeMode(scope, feeKey, mode) {
  calcFeeModes[scope][feeKey] = mode;
  const btnP = document.getElementById('btn-mode-percent-' + feeKey + '-' + scope);
  const btnF = document.getElementById('btn-mode-fixed-' + feeKey + '-' + scope);
  const cP = document.getElementById('container-percent-' + feeKey + '-' + scope);
  const cF = document.getElementById('container-fixed-' + feeKey + '-' + scope);
  const display = document.getElementById('val-' + (feeKey === 'lawyerBuyer' ? 'lawyer-buyer' : feeKey) + '-' + scope);

  if (mode === 'percent') {
    if (btnP) btnP.classList.add('active');
    if (btnF) btnF.classList.remove('active');
    if (cP) cP.style.display = 'block';
    if (cF) cF.style.display = 'none';
    const sliderId = feeKey === 'lawyerBuyer' ? 'rate-lawyer-buyer-c' : ('rate-' + feeKey + '-' + scope);
    const slider = document.getElementById(sliderId);
    if (slider && display) {
      const v = parseFloat(slider.value).toFixed(1) + '%';
      if (display.tagName === 'INPUT') display.value = v; else display.textContent = v;
    }
  } else {
    if (btnF) btnF.classList.add('active');
    if (btnP) btnP.classList.remove('active');
    if (cP) cP.style.display = 'none';
    if (cF) cF.style.display = 'block';
    if (display) { const fixedTxt = calcT('פיקס', 'Fixed'); if (display.tagName === 'INPUT') display.value = fixedTxt; else display.textContent = fixedTxt; }
  }
  calculate();
}

function onFixedFeeInput(scope, feeKey) {
  const el = document.getElementById('fixed-' + feeKey + '-' + scope);
  const v = calcParse(el.value);
  el.value = v > 0 ? v.toLocaleString('he-IL') : '';
  calcFixedFees[scope][feeKey] = v;
  calculate();
}

function enableEditablePercent(input, scope, feeKey) {
  if (calcFeeModes[scope] && calcFeeModes[scope][feeKey] !== 'percent') { input.blur(); return; }
  input.readOnly = false;
  input.classList.add('editing');
  input.value = input.value.replace('%', '');
  input.select();
}

function disableEditablePercent(input, scope, feeKey) {
  input.readOnly = true;
  input.classList.remove('editing');
  let v = parseFloat(input.value);
  if (isNaN(v) || v < 0) v = 0;
  if (v > 100) v = 100;
  input.value = v + '%';
  const sliderId = feeKey === 'lawyerBuyer' ? 'rate-lawyer-buyer-c' : ('rate-' + feeKey + '-' + scope);
  const slider = document.getElementById(sliderId);
  if (slider) slider.value = v;
  calculate();
}

function onCustomPercentInput(input) {
  let v = input.value.replace(/[^0-9.]/g, '');
  const parts = v.split('.');
  if (parts.length > 2) v = parts[0] + '.' + parts.slice(1).join('');
  input.value = v;
  calculate();
}

function toggleMortgageField(scope) {
  const on = document.getElementById(scope + '-mortgage-toggle').checked;
  document.getElementById('container-mortgage-val-' + scope).style.display = on ? 'block' : 'none';
  calculate();
}
function toggleAppraisalField(scope) {
  const on = document.getElementById(scope + '-appraisal-toggle').checked;
  document.getElementById('container-appraisal-val-' + scope).style.display = on ? 'block' : 'none';
  calculate();
}
function toggleGovFeesCard() {
  const card = document.getElementById('gov-fees-card-sh');
  if (card) card.classList.toggle('collapsed');
}
function toggleClientCard() {
  const card = document.getElementById('client-card');
  if (card) card.classList.toggle('collapsed');
}
function onCustomFeesInput() {
  calcFeesCustom = true;
  const el = document.getElementById('fees-c');
  const v = calcParse(el.value);
  el.value = v > 0 ? v.toLocaleString('he-IL') : '0';
  calculate();
}
function onCustomContractorFeeInput() {
  const el = document.getElementById('custom-contractor-fee-c');
  const v = calcParse(el.value);
  el.value = v > 0 ? v.toLocaleString('he-IL') : '';
  calculate();
}
function toggleIndexSection() {
  const on = document.getElementById('c-index-toggle').checked;
  const container = document.getElementById('c-index-inputs-container');
  const label = document.getElementById('c-index-toggle-label');
  if (container) { container.style.opacity = on ? '1' : '0.4'; container.style.pointerEvents = on ? 'auto' : 'none'; }
  if (label) label.textContent = on ? calcT('פעיל (העסקה צמודה)', 'Active (linked deal)') : calcT('לא פעיל (הקבלן סופג את המדד)', 'Off (developer absorbs the index)');
  calculate();
}

/* ==========================================================================
   Purchase-tax breakdown (rendered bilingually from main.js math)
   ========================================================================== */
function renderTaxBrackets(price, type) {
  if (price <= 0) {
    return '<div class="txcalc-bracket-row">' + calcT('הזינו מחיר נכס כדי לראות את פירוט מדרגות המס.', 'Enter a property price to see the tax bracket breakdown.') + '</div>';
  }
  if (type === 'disabled' && typeof currentDisabledSubType !== 'undefined') currentDisabledSubType = 'single';
  const res = computeTaxBreakdown(price, type, false);
  let idx = 1, html = '';
  res.rows.forEach(function (r) {
    const pct = r.rate * 100;
    const rateStr = pct % 1 === 0 ? pct.toFixed(0) : pct.toFixed(1);
    let range;
    if (r.from === 0 && r.to === Infinity) {
      range = calcT('על מלוא שווי הרכישה', 'on the full purchase value');
    } else if (r.to === Infinity) {
      range = calcT('מעל ' + calcFmt(r.from) + ' ₪', 'above ' + calcFmt(r.from) + ' NIS');
    } else {
      range = calcT('מ-' + calcFmt(r.from) + ' ₪ עד ' + calcFmt(r.to) + ' ₪', calcFmt(r.from) + '–' + calcFmt(r.to) + ' NIS');
    }
    const label = calcT('מדרגה ' + idx + ' (' + rateStr + '%): ' + range, 'Bracket ' + idx + ' (' + rateStr + '%): ' + range);
    const val = r.rate === 0 ? calcT('0 ₪ (פטור)', 'Exempt') : calcCur(r.tax);
    html += '<div class="txcalc-bracket-row' + (r.rate === 0 ? '' : ' taxable') + '"><span>' + label + '</span><span>' + val + '</span></div>';
    idx++;
  });
  return html;
}

/* ==========================================================================
   SECOND-HAND calculator
   ========================================================================== */
function recalcSecondHand() {
  const price = calcParse(document.getElementById('price-sh').value);
  const reno = calcParse(document.getElementById('renovation-sh').value);

  const type = calcBuyerType.sh;
  const tax = computeTaxBreakdown(price, type, false).total;
  document.getElementById('sh-brackets-list').innerHTML = renderTaxBrackets(price, type);

  // Brokerage
  let brokerRate = parseFloat((document.getElementById('val-brokerage-sh').value || '').replace('%', '')) / 100;
  if (isNaN(brokerRate)) brokerRate = 0;
  let brokerBase = calcFeeModes.sh.brokerage === 'percent' ? price * brokerRate : calcFixedFees.sh.brokerage;
  const brokerVat = brokerBase * CALC_VAT_RATE;
  const brokerTotal = brokerBase + brokerVat;

  // Representing lawyer
  let lawyerRate = parseFloat((document.getElementById('val-lawyer-sh').value || '').replace('%', '')) / 100;
  if (isNaN(lawyerRate)) lawyerRate = 0;
  let lawyerBase = calcFeeModes.sh.lawyer === 'percent' ? price * lawyerRate : calcFixedFees.sh.lawyer;
  const lawyerVat = lawyerBase * CALC_VAT_RATE;
  const lawyerTotal = lawyerBase + lawyerVat;

  // Financing
  const hasMortgage = document.getElementById('sh-mortgage-toggle').checked;
  const mortgageVal = calcParse(document.getElementById('mortgage-val-sh').value);
  const mortgageCost = hasMortgage ? Math.round(mortgageVal * (1 + CALC_VAT_RATE)) : 0;
  const hasAppraisal = document.getElementById('sh-appraisal-toggle').checked;
  const appraisalVal = calcParse(document.getElementById('appraisal-val-sh').value);
  const appraisalCost = hasAppraisal ? appraisalVal : 0;

  // Government registry fees
  const feeIds = [['sh-fee-tabu', GOV_FEE.tabu], ['sh-fee-joint', GOV_FEE.joint], ['sh-fee-warn-buyer', GOV_FEE.warnBuyer],
    ['sh-fee-warn-bank', GOV_FEE.warnBank], ['sh-fee-mortgage', GOV_FEE.mortgage], ['sh-fee-ownership', GOV_FEE.ownership],
    ['sh-fee-tabu-after', GOV_FEE.tabuAfter]];
  let govFees = 0;
  feeIds.forEach(function (f) { const el = document.getElementById(f[0]); if (el && el.checked) govFees += f[1]; });
  document.getElementById('sh-gov-fees-total-badge').textContent = calcCur(govFees);

  // Sub-labels
  const mortgageTotalDisplay = Math.round(mortgageVal * (1 + CALC_VAT_RATE));
  document.getElementById('sh-mortgage-sub').textContent = calcT(
    'עלות משוערת: ' + calcFmt(mortgageVal) + ' ₪ + מע״מ (' + calcFmt(mortgageTotalDisplay) + ' ₪ סה״כ)',
    'Estimated: ₪ ' + calcFmt(mortgageVal) + ' + VAT (₪ ' + calcFmt(mortgageTotalDisplay) + ' total)');
  document.getElementById('sh-appraisal-sub').textContent = calcT(
    'שמאי הסדר: כ-1,000–2,000 ₪ | שמאות מוקדמת: ' + calcFmt(appraisalVal) + ' ₪ ויותר',
    'Lender appraiser: ~₪1,000–2,000 | Early appraisal: ₪ ' + calcFmt(appraisalVal) + ' and up');

  const addCosts = tax + brokerTotal + lawyerTotal + reno + mortgageCost + appraisalCost + govFees;
  const grand = price + addCosts;

  // Render table
  setText('tbl-sh-price', calcFmt(price));
  setText('tbl-sh-tax', calcFmt(tax));
  setText('tbl-sh-lawyer', calcFmt(lawyerTotal));
  setText('tbl-sh-broker', calcFmt(brokerTotal));
  setText('tbl-sh-reno', calcFmt(reno));
  setText('tbl-sh-gov-fees', calcFmt(govFees));
  rowDisplay('tbl-sh-row-mortgage', hasMortgage); setText('tbl-sh-mortgage', calcFmt(mortgageCost));
  rowDisplay('tbl-sh-row-appraisal', hasAppraisal); setText('tbl-sh-appraisal', calcFmt(appraisalCost));
  setText('tbl-sh-addcosts', calcFmt(addCosts));
  animateValue('tbl-sh-grandtotal', grand, true);

  // Fee mini-breakdowns
  setText('sh-broker-base', calcCur(brokerBase)); setText('sh-broker-vat', calcCur(brokerVat)); setText('sh-broker-total', calcCur(brokerTotal));
  setText('sh-lawyer-base', calcCur(lawyerBase)); setText('sh-lawyer-vat', calcCur(lawyerVat)); setText('sh-lawyer-total', calcCur(lawyerTotal));

  drawDonutChart('sh', price, addCosts);

  calcLastReport = {
    scope: 'sh', price: price, addCosts: addCosts, grand: grand, type: type,
    taxRows: computeTaxBreakdown(price, type, false).rows, taxTotal: tax,
    lines: [
      { he: 'מס רכישה (מדורג 2026)', en: 'Purchase tax (2026 brackets)', val: tax },
      { he: 'שכר טרחת עו״ד מייצג (כולל מע״מ)', en: 'Representing attorney fee (incl. VAT)', val: lawyerTotal },
      { he: 'דמי תיווך (כולל מע״מ)', en: 'Broker commission (incl. VAT)', val: brokerTotal },
      { he: 'שיפוץ והתאמות נכס', en: 'Renovation & fit-out', val: reno, skipZero: true },
      { he: 'אגרות רישום ממשלתיות', en: 'Government registry fees', val: govFees },
      { he: 'ליווי יועץ משכנתאות (כולל מע״מ)', en: 'Mortgage advisor (incl. VAT)', val: mortgageCost, skipZero: true },
      { he: 'שמאות', en: 'Appraisal', val: appraisalCost, skipZero: true }
    ]
  };
}

/* ==========================================================================
   CONTRACTOR (new-build) calculator
   ========================================================================== */
function recalcContractor() {
  const price = calcParse(document.getElementById('price-c').value);
  const upgrades = calcParse(document.getElementById('upgrades-c').value);
  const fees = calcParse(document.getElementById('fees-c').value);

  const type = calcBuyerType.c;
  const tax = computeTaxBreakdown(price, type, false).total;
  document.getElementById('c-brackets-list').innerHTML = renderTaxBrackets(price, type);

  // Buyer's representing lawyer
  let buyerRate = parseFloat((document.getElementById('val-lawyer-buyer-c').value || '').replace('%', '')) / 100;
  if (isNaN(buyerRate)) buyerRate = 0;
  let buyerBase = calcFeeModes.c.lawyerBuyer === 'percent' ? price * buyerRate : calcFixedFees.c.lawyerBuyer;
  const buyerVat = buyerBase * CALC_VAT_RATE;
  const buyerTotal = buyerBase + buyerVat;
  setText('c-lawyer-buyer-base', calcCur(buyerBase)); setText('c-lawyer-buyer-vat', calcCur(buyerVat)); setText('c-lawyer-buyer-total', calcCur(buyerTotal));

  // Contractor's lawyer fee (statutory cap)
  let devBase = 0, capped = false;
  if (price > 0) {
    if (price <= CONTRACTOR_LAWYER_CEILING_PRICE) {
      devBase = Math.min(price * 0.005, CONTRACTOR_LAWYER_CAP);
      capped = true;
    } else {
      const custom = calcParse((document.getElementById('custom-contractor-fee-c') || {}).value);
      devBase = custom > 0 ? custom : CONTRACTOR_LAWYER_CAP;
    }
  }
  const devVat = devBase * CALC_VAT_RATE;
  const devTotal = devBase + devVat;

  const statusEl = document.getElementById('val-lawyer-c-status');
  const warnEl = document.getElementById('c-lawyer-warning');
  const customWrap = document.getElementById('c-custom-contractor-fee-wrapper');
  if (price > CONTRACTOR_LAWYER_CEILING_PRICE) {
    statusEl.textContent = calcT('לא מוגבל בחוק', 'Not capped (luxury)');
    statusEl.classList.add('is-warning'); statusEl.classList.remove('is-ok');
    if (warnEl) warnEl.style.display = 'block';
    if (customWrap) customWrap.style.display = 'block';
  } else {
    statusEl.textContent = calcT('מוגבל בחוק', 'Capped by law');
    statusEl.classList.add('is-ok'); statusEl.classList.remove('is-warning');
    if (warnEl) warnEl.style.display = 'none';
    if (customWrap) customWrap.style.display = 'none';
  }
  setText('c-lawyer-base', calcCur(devBase)); setText('c-lawyer-vat', calcCur(devVat)); setText('c-lawyer-total', calcCur(devTotal));

  // Financing
  const hasMortgage = document.getElementById('c-mortgage-toggle').checked;
  const mortgageVal = calcParse(document.getElementById('mortgage-val-c').value);
  const mortgageCost = hasMortgage ? Math.round(mortgageVal * (1 + CALC_VAT_RATE)) : 0;
  const hasAppraisal = document.getElementById('c-appraisal-toggle').checked;
  const appraisalVal = calcParse(document.getElementById('appraisal-val-c').value);
  const appraisalCost = hasAppraisal ? appraisalVal : 0;
  const mortgageTotalDisplay = Math.round(mortgageVal * (1 + CALC_VAT_RATE));
  document.getElementById('c-mortgage-sub').textContent = calcT(
    'עלות משוערת: ' + calcFmt(mortgageVal) + ' ₪ + מע״מ (' + calcFmt(mortgageTotalDisplay) + ' ₪ סה״כ)',
    'Estimated: ₪ ' + calcFmt(mortgageVal) + ' + VAT (₪ ' + calcFmt(mortgageTotalDisplay) + ' total)');
  document.getElementById('c-appraisal-sub').textContent = calcT(
    'שמאי הסדר: כ-1,000–2,000 ₪ | שמאות מוקדמת: ' + calcFmt(appraisalVal) + ' ₪ ויותר',
    'Lender appraiser: ~₪1,000–2,000 | Early appraisal: ₪ ' + calcFmt(appraisalVal) + ' and up');

  // Index linkage (Amendment 9 simulation)
  const linked = document.getElementById('c-index-toggle').checked;
  const months = parseInt(document.getElementById('c-index-months').value, 10) || 0;
  const annual = parseFloat(document.getElementById('c-index-rate').value) || 0;
  const down = parseFloat(document.getElementById('c-downpayment').value) || 20;
  const methodSel = document.getElementById('c-index-method');
  const method = methodSel.value;
  // Localise the (plain-text) <select> options for the active language
  if (methodSel.options.length >= 2) {
    methodSel.options[0].textContent = calcT('פריסת תשלומים אחידה (ריאלי)', 'Even payment spread (realistic)');
    methodSel.options[1].textContent = calcT('תשלום מלא במסירה (שמרני)', 'Full payment at delivery (conservative)');
  }
  const linkedBase = price * Math.max(0, (100 - down) / 100) * 0.5;     // ≤40% of price is linkable (Amendment 9)
  const monthly = Math.pow(1 + annual / 100, 1 / 12) - 1;
  const growth = Math.pow(1 + monthly, months) - 1;
  const scheduleCoeff = method === 'realistic' ? 0.5 : 1.0;
  const indexCost = linked ? Math.round(linkedBase * growth * scheduleCoeff) : 0;

  if (linked) {
    setText('c-linked-sum', calcCur(linkedBase));
    setText('c-linked-pct', (growth * 100).toFixed(2) + '%');
    setText('c-linked-cost', calcCur(indexCost));
  } else {
    setText('c-linked-sum', calcCur(0));
    setText('c-linked-pct', '0.00%');
    setText('c-linked-cost', calcT('0 ₪ (הקבלן סופג)', '₪ 0 (developer absorbs)'));
  }

  const addCosts = tax + devTotal + buyerTotal + mortgageCost + appraisalCost + indexCost + upgrades + fees;
  const grand = price + addCosts;

  setText('tbl-c-price', calcFmt(price));
  setText('tbl-c-tax', calcFmt(tax));
  setText('tbl-c-lawyer-dev', calcFmt(devTotal));
  setText('tbl-c-lawyer-buyer', calcFmt(buyerTotal));
  rowDisplay('tbl-c-row-mortgage', hasMortgage); setText('tbl-c-mortgage', calcFmt(mortgageCost));
  rowDisplay('tbl-c-row-appraisal', hasAppraisal); setText('tbl-c-appraisal', calcFmt(appraisalCost));
  setText('tbl-c-index', linked ? calcFmt(indexCost) : calcT('0 (הקבלן סופג)', '0 (absorbed)'));
  setText('tbl-c-upgrades', calcFmt(upgrades));
  setText('tbl-c-fees', calcFmt(fees));
  setText('tbl-c-addcosts', calcFmt(addCosts));
  animateValue('tbl-c-grandtotal', grand, true);

  drawDonutChart('c', price, addCosts);

  calcLastReport = {
    scope: 'c', price: price, addCosts: addCosts, grand: grand, type: type,
    taxRows: computeTaxBreakdown(price, type, false).rows, taxTotal: tax,
    lines: [
      { he: 'מס רכישה (מדורג 2026)', en: 'Purchase tax (2026 brackets)', val: tax },
      { he: 'שכר טרחת עו״ד הקבלן (כולל מע״מ)', en: "Developer's attorney fee (incl. VAT)", val: devTotal },
      { he: 'שכר טרחת עו״ד הקונה (כולל מע״מ)', en: "Buyer's attorney fee (incl. VAT)", val: buyerTotal },
      { he: 'ליווי יועץ משכנתאות (כולל מע״מ)', en: 'Mortgage advisor (incl. VAT)', val: mortgageCost, skipZero: true },
      { he: 'שמאות', en: 'Appraisal', val: appraisalCost, skipZero: true },
      { he: 'אומדן הצמדה למדד תשומות הבנייה', en: 'Estimated construction-index linkage', val: indexCost, skipZero: true },
      { he: 'תקציב שדרוגים ותוספות קבלן', en: 'Upgrades & developer extras', val: upgrades, skipZero: true },
      { he: 'תשריטים ואגרות רישום', en: 'Plans & registry fees', val: fees }
    ]
  };
}

/* ==========================================================================
   Donut chart (gold segment over a subtle navy ring)
   ========================================================================== */
function drawDonutChart(scope, basePrice, addCosts) {
  const segment = document.getElementById(scope + '-chart-segment');
  const bg = document.getElementById(scope + '-chart-bg-segment');
  const pctText = document.getElementById(scope + '-chart-percent');
  if (!segment) return;
  const circumference = 502.65;

  if (basePrice <= 0) {
    segment.setAttribute('stroke-dashoffset', circumference);
    if (pctText) pctText.textContent = '0%';
    segment.setAttribute('data-value', '0'); segment.setAttribute('data-pct', '0');
    if (bg) { bg.setAttribute('data-value', '0'); bg.setAttribute('data-pct', '0'); }
    return;
  }
  const total = basePrice + addCosts;
  const pct = (addCosts / total) * 100;
  segment.setAttribute('stroke-dasharray', circumference);
  segment.setAttribute('stroke-dashoffset', circumference - (pct / 100) * circumference);
  if (pctText) pctText.textContent = pct.toFixed(1) + '%';
  segment.setAttribute('data-value', addCosts); segment.setAttribute('data-pct', pct.toFixed(1));
  if (bg) { bg.setAttribute('data-value', basePrice); bg.setAttribute('data-pct', (100 - pct).toFixed(1)); }
}

function initChartTooltips(scope) {
  const bg = document.getElementById(scope + '-chart-bg-segment');
  const seg = document.getElementById(scope + '-chart-segment');
  const tooltip = document.getElementById(scope + '-chart-tooltip');
  if (!seg || !tooltip) return;
  const container = tooltip.parentElement;
  const segs = [
    { el: bg, he: 'מחיר העסקה (נכס)', en: 'Property price' },
    { el: seg, he: 'עלויות נלוות', en: 'Additional costs' }
  ];
  segs.forEach(function (s) {
    if (!s.el) return;
    const show = function () {
      const val = parseInt(s.el.getAttribute('data-value'), 10) || 0;
      const pct = s.el.getAttribute('data-pct') || '0.0';
      tooltip.innerHTML = '<strong>' + calcT(s.he, s.en) + '</strong><br>' + calcCur(val) + ' (' + pct + '%)';
      tooltip.classList.add('visible');
    };
    s.el.addEventListener('mouseenter', show);
    s.el.addEventListener('click', show);                 // tap support on mobile
    s.el.addEventListener('mousemove', function (e) {
      const rect = container.getBoundingClientRect();
      tooltip.style.left = (e.clientX - rect.left) + 'px';
      tooltip.style.top = (e.clientY - rect.top) + 'px';
    });
    s.el.addEventListener('mouseleave', function () { tooltip.classList.remove('visible'); });
  });
}

/* ==========================================================================
   Help tooltips — tap to toggle on touch devices
   ========================================================================== */
function initCalcTipTaps() {
  document.querySelectorAll('.txcalc-tip').forEach(function (tip) {
    tip.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      const open = tip.classList.contains('open');
      document.querySelectorAll('.txcalc-tip.open').forEach(function (t) { t.classList.remove('open'); });
      if (!open) tip.classList.add('open');
    });
    tip.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); tip.classList.toggle('open'); }
    });
  });
  document.addEventListener('click', function () {
    document.querySelectorAll('.txcalc-tip.open').forEach(function (t) { t.classList.remove('open'); });
  });
}

/* ==========================================================================
   Count-up animation for headline totals (respects reduced-motion)
   ========================================================================== */
function animateValue(id, target, currency) {
  const el = document.getElementById(id);
  if (!el) return;
  const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const render = function (n) { el.textContent = currency ? calcCur(n) : calcFmt(n); };
  if (reduce) { render(target); return; }
  const from = parseInt((el.getAttribute('data-raw') || '0'), 10) || 0;
  el.setAttribute('data-raw', String(Math.round(target)));
  if (from === Math.round(target)) { render(target); return; }
  const dur = 450, t0 = performance.now();
  function step(now) {
    const p = Math.min(1, (now - t0) / dur);
    const eased = 1 - Math.pow(1 - p, 3);
    render(from + (target - from) * eased);
    if (p < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

function setText(id, txt) { const el = document.getElementById(id); if (el) el.textContent = txt; }
function rowDisplay(id, on) { const el = document.getElementById(id); if (el) el.style.display = on ? 'table-row' : 'none'; }

/* ==========================================================================
   Share link (copies the current state into the URL)
   ========================================================================== */
function shareCalculation() {
  const url = new URL(window.location.href);
  const p = url.searchParams;
  const set = function (k, v) { p.set(k, v); };

  if (document.getElementById('price-sh')) {
    set('price_sh', calcParse(document.getElementById('price-sh').value));
    set('buyer_sh', calcBuyerType.sh);
    set('broker_sh', parseFloat((document.getElementById('val-brokerage-sh').value || '0').replace('%', '')) || 0);
    set('lawyer_sh', parseFloat((document.getElementById('val-lawyer-sh').value || '0').replace('%', '')) || 0);
    set('reno_sh', calcParse(document.getElementById('renovation-sh').value));
    set('sh_gov_flags', ['sh-fee-tabu', 'sh-fee-joint', 'sh-fee-warn-buyer', 'sh-fee-warn-bank', 'sh-fee-mortgage', 'sh-fee-ownership', 'sh-fee-tabu-after']
      .map(function (id) { return document.getElementById(id).checked ? '1' : '0'; }).join(''));
    set('mode_broker_sh', calcFeeModes.sh.brokerage); set('val_broker_sh_fixed', calcFixedFees.sh.brokerage);
    set('mode_lawyer_sh', calcFeeModes.sh.lawyer); set('val_lawyer_sh_fixed', calcFixedFees.sh.lawyer);
    set('sh_mortgage', document.getElementById('sh-mortgage-toggle').checked ? '1' : '0');
    set('sh_mortgage_val', calcParse(document.getElementById('mortgage-val-sh').value));
    set('sh_appraisal', document.getElementById('sh-appraisal-toggle').checked ? '1' : '0');
    set('sh_appraisal_val', calcParse(document.getElementById('appraisal-val-sh').value));
  } else if (document.getElementById('price-c')) {
    set('price_c', calcParse(document.getElementById('price-c').value));
    set('buyer_c', calcBuyerType.c);
    set('lawyer_c', parseFloat((document.getElementById('val-lawyer-buyer-c').value || '0').replace('%', '')) || 0);
    set('upgrades_c', calcParse(document.getElementById('upgrades-c').value));
    set('custom_contractor_fee', calcParse((document.getElementById('custom-contractor-fee-c') || {}).value));
    set('mode_lawyer_buyer_c', calcFeeModes.c.lawyerBuyer); set('val_lawyer_buyer_c_fixed', calcFixedFees.c.lawyerBuyer);
    set('c_months', document.getElementById('c-index-months').value);
    set('c_rate', document.getElementById('c-index-rate').value);
    set('c_down', document.getElementById('c-downpayment').value);
    set('c_method', document.getElementById('c-index-method').value);
    set('c_index_active', document.getElementById('c-index-toggle').checked ? '1' : '0');
    set('c_fees', calcParse(document.getElementById('fees-c').value));
    set('c_mortgage', document.getElementById('c-mortgage-toggle').checked ? '1' : '0');
    set('c_mortgage_val', calcParse(document.getElementById('mortgage-val-c').value));
    set('c_appraisal', document.getElementById('c-appraisal-toggle').checked ? '1' : '0');
    set('c_appraisal_val', calcParse(document.getElementById('appraisal-val-c').value));
  }
  set('name', (document.getElementById('client-name') || {}).value || '');
  set('addr', (document.getElementById('property-address') || {}).value || '');
  set('notes', (document.getElementById('calculation-notes') || {}).value || '');

  navigator.clipboard.writeText(url.toString()).then(function () {
    alert(calcT('הקישור לשיתוף החישוב הועתק ללוח בהצלחה!', 'Share link copied to clipboard!'));
  }).catch(function () {
    window.prompt(calcT('העתיקו את הקישור:', 'Copy the link:'), url.toString());
  });
}

function restoreSecondHandFromUrl() {
  const p = new URLSearchParams(window.location.search);
  const setVal = function (id, v) { const el = document.getElementById(id); if (el) el.value = v; };
  if (p.has('price_sh')) setVal('price-sh', (parseInt(p.get('price_sh'), 10) || 0).toLocaleString('he-IL'));
  if (p.has('reno_sh')) setVal('renovation-sh', (parseInt(p.get('reno_sh'), 10) || 0).toLocaleString('he-IL'));
  if (p.has('buyer_sh')) calcBuyerType.sh = p.get('buyer_sh');
  if (p.has('broker_sh')) { const v = parseFloat(p.get('broker_sh')); setVal('rate-brokerage-sh', v); setVal('val-brokerage-sh', v + '%'); }
  if (p.has('lawyer_sh')) { const v = parseFloat(p.get('lawyer_sh')); setVal('rate-lawyer-sh', v); setVal('val-lawyer-sh', v + '%'); }
  if (p.has('sh_gov_flags')) {
    const f = p.get('sh_gov_flags');
    const ids = ['sh-fee-tabu', 'sh-fee-joint', 'sh-fee-warn-buyer', 'sh-fee-warn-bank', 'sh-fee-mortgage', 'sh-fee-ownership', 'sh-fee-tabu-after'];
    ids.forEach(function (id, i) { const el = document.getElementById(id); if (el && i < f.length) el.checked = f[i] === '1'; });
  }
  if (p.has('mode_broker_sh')) {
    calcFeeModes.sh.brokerage = p.get('mode_broker_sh');
    calcFixedFees.sh.brokerage = parseInt(p.get('val_broker_sh_fixed'), 10) || 0;
    setVal('fixed-brokerage-sh', calcFixedFees.sh.brokerage > 0 ? calcFixedFees.sh.brokerage.toLocaleString('he-IL') : '');
    setFeeMode('sh', 'brokerage', calcFeeModes.sh.brokerage);
  }
  if (p.has('mode_lawyer_sh')) {
    calcFeeModes.sh.lawyer = p.get('mode_lawyer_sh');
    calcFixedFees.sh.lawyer = parseInt(p.get('val_lawyer_sh_fixed'), 10) || 0;
    setVal('fixed-lawyer-sh', calcFixedFees.sh.lawyer > 0 ? calcFixedFees.sh.lawyer.toLocaleString('he-IL') : '');
    setFeeMode('sh', 'lawyer', calcFeeModes.sh.lawyer);
  }
  if (p.has('sh_mortgage')) { const on = p.get('sh_mortgage') === '1'; document.getElementById('sh-mortgage-toggle').checked = on; document.getElementById('container-mortgage-val-sh').style.display = on ? 'block' : 'none'; }
  if (p.has('sh_mortgage_val')) setVal('mortgage-val-sh', (parseInt(p.get('sh_mortgage_val'), 10) || 0).toLocaleString('he-IL'));
  if (p.has('sh_appraisal')) { const on = p.get('sh_appraisal') === '1'; document.getElementById('sh-appraisal-toggle').checked = on; document.getElementById('container-appraisal-val-sh').style.display = on ? 'block' : 'none'; }
  if (p.has('sh_appraisal_val')) setVal('appraisal-val-sh', (parseInt(p.get('sh_appraisal_val'), 10) || 0).toLocaleString('he-IL'));
  restoreClientMeta(p);
}

function restoreContractorFromUrl() {
  const p = new URLSearchParams(window.location.search);
  const setVal = function (id, v) { const el = document.getElementById(id); if (el) el.value = v; };
  if (p.has('price_c')) setVal('price-c', (parseInt(p.get('price_c'), 10) || 0).toLocaleString('he-IL'));
  if (p.has('upgrades_c')) setVal('upgrades-c', (parseInt(p.get('upgrades_c'), 10) || 0).toLocaleString('he-IL'));
  if (p.has('c_fees')) { setVal('fees-c', (parseInt(p.get('c_fees'), 10) || 0).toLocaleString('he-IL')); calcFeesCustom = true; }
  if (p.has('custom_contractor_fee')) { const v = parseInt(p.get('custom_contractor_fee'), 10) || 0; setVal('custom-contractor-fee-c', v > 0 ? v.toLocaleString('he-IL') : ''); }
  if (p.has('buyer_c')) calcBuyerType.c = p.get('buyer_c');
  if (p.has('lawyer_c')) { const v = parseFloat(p.get('lawyer_c')); setVal('rate-lawyer-buyer-c', v); setVal('val-lawyer-buyer-c', v + '%'); }
  if (p.has('mode_lawyer_buyer_c')) {
    calcFeeModes.c.lawyerBuyer = p.get('mode_lawyer_buyer_c');
    calcFixedFees.c.lawyerBuyer = parseInt(p.get('val_lawyer_buyer_c_fixed'), 10) || 0;
    setVal('fixed-lawyerBuyer-c', calcFixedFees.c.lawyerBuyer > 0 ? calcFixedFees.c.lawyerBuyer.toLocaleString('he-IL') : '');
    setFeeMode('c', 'lawyerBuyer', calcFeeModes.c.lawyerBuyer);
  }
  if (p.has('c_months')) setVal('c-index-months', p.get('c_months'));
  if (p.has('c_rate')) setVal('c-index-rate', p.get('c_rate'));
  if (p.has('c_down')) setVal('c-downpayment', p.get('c_down'));
  if (p.has('c_method')) setVal('c-index-method', p.get('c_method'));
  if (p.has('c_index_active')) { const on = p.get('c_index_active') === '1'; document.getElementById('c-index-toggle').checked = on; toggleIndexSection(); }
  if (p.has('c_mortgage')) { const on = p.get('c_mortgage') === '1'; document.getElementById('c-mortgage-toggle').checked = on; document.getElementById('container-mortgage-val-c').style.display = on ? 'block' : 'none'; }
  if (p.has('c_mortgage_val')) setVal('mortgage-val-c', (parseInt(p.get('c_mortgage_val'), 10) || 0).toLocaleString('he-IL'));
  if (p.has('c_appraisal')) { const on = p.get('c_appraisal') === '1'; document.getElementById('c-appraisal-toggle').checked = on; document.getElementById('container-appraisal-val-c').style.display = on ? 'block' : 'none'; }
  if (p.has('c_appraisal_val')) setVal('appraisal-val-c', (parseInt(p.get('c_appraisal_val'), 10) || 0).toLocaleString('he-IL'));
  restoreClientMeta(p);
}

function restoreClientMeta(p) {
  [['name', 'client-name'], ['addr', 'property-address'], ['notes', 'calculation-notes']].forEach(function (m) {
    if (p.has(m[0])) { const el = document.getElementById(m[1]); if (el) el.value = p.get(m[0]); }
  });
}

/* ==========================================================================
   Branded printable report (same letterhead approach as the tax simulator)
   ========================================================================== */
function printCalcReport() {
  if (!calcLastReport) calculate();
  const r = calcLastReport;
  if (!r) return;
  const isHe = calcIsHe();
  const lang = isHe ? 'he' : 'en';
  const fmt = function (n) { return isHe ? (Math.round(n).toLocaleString('he-IL') + ' ₪') : ('₪ ' + Math.round(n).toLocaleString('en-US')); };

  const logoUrl = new URL((window.location.pathname.indexOf('/en/') !== -1 ? '../../../' : '../../') + 'assets/logo.png', window.location.href).href;
  const dateStr = new Date().toLocaleDateString(isHe ? 'he-IL' : 'en-GB');
  const clientName = (document.getElementById('client-name') || {}).value || '';
  const addr = (document.getElementById('property-address') || {}).value || '';
  const notes = (document.getElementById('calculation-notes') || {}).value || '';

  const typeLabels = {
    single: calcT('דירת מגורים יחידה', 'Single residential home'),
    additional: calcT('דירה נוספת / להשקעה', 'Additional / investment home'),
    immigrant: calcT('עולה חדש', 'New immigrant (oleh)'),
    disabled: calcT('נכה / עיוור (תקנה 11)', 'Disabled / blind (Regulation 11)')
  };

  const L = isHe ? {
    docTitle: r.scope === 'sh' ? 'דוח עלויות רכישת דירה יד שנייה' : 'דוח עלויות רכישת דירה מקבלן',
    firmName: 'משרד עו״ד אלירם אלגרבלי',
    firmTag: 'מקרקעין · מיסוי מקרקעין · נדל״ן',
    reportTitle: r.scope === 'sh' ? 'דוח עלויות — רכישת דירת יד שנייה' : 'דוח עלויות — רכישת דירה מקבלן',
    reportSub: 'אומדן מבוסס נתוני 2026 · נוצר בסימולטור באתר המשרד',
    metaPrice: 'מחיר העסקה', metaType: 'סוג רוכש', metaDate: 'תאריך', metaClient: 'לקוח', metaAddr: 'נכס',
    breakdownTitle: 'פירוט עלויות העסקה', colItem: 'רכיב עלות', colAmount: 'סכום (₪)',
    addCosts: 'עלויות נלוות (סה״כ)', grand: 'סה״כ עלות העסקה (נכס + הוצאות)',
    notesTitle: 'הערות', contact: 'טל׳: 08-6206666 · ארה״ב: ‎+1 (424) 367-8863 · office@madrich.co.il',
    disclaimer: 'דוח זה הופק באמצעות הסימולטור באתר המשרד והוא אומדן ראשוני בלבד לצורכי תכנון פיננסי. אין בו כדי להוות ייעוץ משפטי, חוות דעת או תחליף לתכנון מס וליווי פרטני על ידי עורך דין מקרקעין. הנתונים נכונים למדרגות ולשיעורים שבתוקף בשנת 2026.',
    btnPrint: 'הדפסה / שמירה כ-PDF', btnClose: 'סגירה'
  } : {
    docTitle: r.scope === 'sh' ? 'Resale Purchase Cost Report' : 'New-Build Purchase Cost Report',
    firmName: 'Adv. Eliram Elgarably Law Office',
    firmTag: 'Real Estate · Property Taxation · Conveyancing',
    reportTitle: r.scope === 'sh' ? 'Cost Report — Resale Apartment Purchase' : 'Cost Report — New-Build Purchase',
    reportSub: 'Estimate based on 2026 figures · generated by the firm\'s online simulator',
    metaPrice: 'Transaction price', metaType: 'Buyer type', metaDate: 'Date', metaClient: 'Client', metaAddr: 'Property',
    breakdownTitle: 'Transaction Cost Breakdown', colItem: 'Cost item', colAmount: 'Amount (NIS)',
    addCosts: 'Additional costs (total)', grand: 'Total transaction cost (property + costs)',
    notesTitle: 'Notes', contact: 'Tel: 08-6206666 · US: +1 (424) 367-8863 · office@madrich.co.il',
    disclaimer: 'This report was generated by the simulator on the firm\'s website and is a preliminary estimate for financial-planning purposes only. It does not constitute legal advice or an opinion, nor does it replace individual tax planning and representation by a qualified real estate attorney. Figures reflect the brackets and rates in force in 2026.',
    btnPrint: 'Print / Save as PDF', btnClose: 'Close'
  };

  const itemRows = r.lines.filter(function (l) { return !(l.skipZero && (!l.val || l.val <= 0)); })
    .map(function (l) { return '<tr><td>' + (isHe ? l.he : l.en) + '</td><td>' + fmt(l.val) + '</td></tr>'; }).join('');

  const metaCards = [
    '<div class="meta-card"><div class="meta-label">' + L.metaPrice + '</div><div class="meta-value">' + fmt(r.price) + '</div></div>',
    '<div class="meta-card"><div class="meta-label">' + L.metaType + '</div><div class="meta-value">' + (typeLabels[r.type] || '') + '</div></div>',
    '<div class="meta-card"><div class="meta-label">' + L.metaDate + '</div><div class="meta-value">' + dateStr + '</div></div>',
    clientName ? '<div class="meta-card"><div class="meta-label">' + L.metaClient + '</div><div class="meta-value">' + escapeHtml(clientName) + '</div></div>' : ''
  ].join('');

  const html = '<!DOCTYPE html><html lang="' + lang + '" dir="' + (isHe ? 'rtl' : 'ltr') + '"><head><meta charset="UTF-8"><title>' + L.docTitle + '</title>' +
    '<link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700;800&family=Cinzel:wght@600;700&display=swap" rel="stylesheet">' +
    '<style>' +
    '*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}' +
    'html,body{background:#fff}body{font-family:"Assistant",sans-serif;color:#1C2541}' +
    '.toolbar{position:fixed;top:0;left:0;right:0;display:flex;justify-content:center;gap:10px;padding:12px;background:#0A1128;z-index:10}' +
    '.toolbar button{font-family:"Assistant",sans-serif;font-size:15px;font-weight:600;padding:8px 22px;border-radius:4px;cursor:pointer;border:1px solid #C5A880}' +
    '.toolbar .primary{background:#C5A880;color:#0A1128}.toolbar .secondary{background:transparent;color:#C5A880}' +
    '.screen-offset{height:64px}.page{width:210mm;margin:0 auto;padding:0 14mm 8mm}' +
    '.gold-rule{height:5px;background:linear-gradient(90deg,#8F724C,#E5C494,#8F724C)}' +
    '.report-header{text-align:center;padding:9mm 0 5mm;border-bottom:1px solid rgba(197,168,128,.5)}.report-header img{height:64px}' +
    '.firm-name{font-family:' + (isHe ? '"Assistant",sans-serif' : '"Cinzel",serif') + ';font-size:15px;font-weight:700;letter-spacing:' + (isHe ? '.05em' : '.3em') + ';color:#0A1128;margin-top:3mm}' +
    '.firm-tag{font-size:10.5px;color:#8F724C;letter-spacing:.12em;margin-top:1mm}' +
    'h1{font-size:23px;font-weight:800;color:#0A1128;text-align:center;margin-top:7mm}.report-sub{text-align:center;color:#6C7A89;font-size:11.5px;margin-top:1.5mm}' +
    '.meta-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;margin-top:7mm}' +
    '.meta-card{border:1px solid rgba(197,168,128,.45);border-radius:6px;padding:3.5mm 2mm;text-align:center;background:#FCFBF9}' +
    '.meta-label{font-size:9.5px;font-weight:600;color:#8F724C;letter-spacing:.05em}.meta-value{font-size:13px;font-weight:700;color:#0A1128;margin-top:1.5mm}' +
    (addr ? '.addr-line{margin-top:3mm;font-size:11px;color:#6C7A89;text-align:center}' : '') +
    '.total-band{margin-top:6mm;background:linear-gradient(135deg,#0A1128,#101F42);border-radius:8px;padding:5.5mm 8mm;display:flex;align-items:center;justify-content:space-between}' +
    '.total-band .label{color:#F4F5F7;font-size:14px;font-weight:600}.total-band .amount{color:#E5C494;font-size:26px;font-weight:800}' +
    'h2{font-size:13.5px;font-weight:700;color:#0A1128;border-inline-start:3px solid #C5A880;padding-inline-start:3mm;margin:7mm 0 3mm}' +
    'table{width:100%;border-collapse:collapse;font-size:12px}th{background:#0A1128;color:#E5C494;font-weight:600;padding:2.6mm 3mm;text-align:' + (isHe ? 'right' : 'left') + '}' +
    'th:last-child,td:last-child{text-align:' + (isHe ? 'left' : 'right') + '}td{padding:2.6mm 3mm;border-bottom:1px solid #ECECEC}tbody tr:nth-child(even) td{background:#FAF8F5}' +
    'tr.sub td{background:rgba(197,168,128,.12);font-weight:700}tr.total-row td{background:rgba(197,168,128,.18);border-top:2px solid #C5A880;border-bottom:none;font-weight:800;font-size:13px;color:#0A1128}' +
    '.callout{margin-top:5mm;border:1px solid rgba(197,168,128,.5);border-radius:6px;background:rgba(197,168,128,.08);padding:3.5mm 4.5mm;font-size:11px;line-height:1.6}' +
    '.report-footer{margin-top:8mm;border-top:1px solid rgba(197,168,128,.5);padding-top:3.5mm;text-align:center}' +
    '.footer-firm{font-size:11px;font-weight:700;color:#0A1128}.footer-contact{font-size:10px;color:#6C7A89;margin-top:1mm;direction:ltr}' +
    '.footer-disclaimer{font-size:8.5px;color:#9AA3AD;line-height:1.55;margin-top:2mm;text-align:justify}' +
    '@page{size:A4;margin:0}@media print{.toolbar,.screen-offset{display:none}.page{width:100%}}' +
    '</style></head><body>' +
    '<div class="toolbar"><button class="primary" onclick="window.print()">' + L.btnPrint + '</button><button class="secondary" onclick="window.close()">' + L.btnClose + '</button></div>' +
    '<div class="screen-offset"></div><div class="gold-rule"></div><div class="page">' +
    '<div class="report-header"><img src="' + logoUrl + '" alt=""><div class="firm-name">' + L.firmName + '</div><div class="firm-tag">' + L.firmTag + '</div></div>' +
    '<h1>' + L.reportTitle + '</h1><div class="report-sub">' + L.reportSub + '</div>' +
    '<div class="meta-grid">' + metaCards + '</div>' +
    (addr ? '<div class="addr-line">' + L.metaAddr + ': ' + escapeHtml(addr) + '</div>' : '') +
    '<div class="total-band"><span class="label">' + L.grand + '</span><span class="amount">' + fmt(r.grand) + '</span></div>' +
    '<h2>' + L.breakdownTitle + '</h2><table><thead><tr><th>' + L.colItem + '</th><th>' + L.colAmount + '</th></tr></thead><tbody>' +
    '<tr><td>' + calcT('מחיר העסקה', 'Transaction price') + '</td><td>' + fmt(r.price) + '</td></tr>' +
    itemRows +
    '<tr class="sub"><td>' + L.addCosts + '</td><td>' + fmt(r.addCosts) + '</td></tr>' +
    '<tr class="total-row"><td>' + L.grand + '</td><td>' + fmt(r.grand) + '</td></tr>' +
    '</tbody></table>' +
    (notes ? '<div class="callout"><strong>' + L.notesTitle + ':</strong> ' + escapeHtml(notes) + '</div>' : '') +
    '<div class="report-footer"><div class="footer-firm">' + L.firmName + '</div><div class="footer-contact">' + L.contact + '</div><div class="footer-disclaimer">* ' + L.disclaimer + '</div></div>' +
    '</div></body></html>';

  const w = window.open('', '_blank');
  if (!w) { alert(calcT('לא ניתן לפתוח את חלון הדוח. אנא אפשרו חלונות קופצים עבור אתר זה.', 'Could not open the report window. Please allow pop-ups for this site.')); return; }
  w.document.write(html);
  w.document.close();
  w.addEventListener('load', function () { setTimeout(function () { w.focus(); w.print(); }, 400); });
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
  });
}
