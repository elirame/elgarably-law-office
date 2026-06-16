/*
   ==========================================================================
   Adv. Eliram Elgarably - Premium Real Estate Law Firm Website
   Interactive Engine & Functionality
   ==========================================================================
*/

// GLOBAL STATE
let currentLanguage = 'he';
let currentPropertyType = 'single'; // 'single', 'additional', 'immigrant', or 'disabled'
let currentDisabledSubType = 'single'; // 'single' or 'additional' — only used by the disabled/blind track
let isGiftProperty = false;

// Disabled / Blind purchase-tax relief (Regulation 11) — 2026 figures
const DISABLED_RATE = 0.005;             // 0.5%
const DISABLED_EXEMPT_CEILING = 1978745; // full exemption ceiling for a single home (2026)
const DISABLED_FLAT_THRESHOLD = 2500000; // single home above this is taxed 0.5% on the WHOLE value

// Real Estate Purchase Tax Brackets (Israel - Updated/Estimated Rates)
const TAX_BRACKETS = {
  single: [
    { limit: 1978745, rate: 0.00 },
    { limit: 2347040, rate: 0.035 },
    { limit: 6055070, rate: 0.05 },
    { limit: 20183565, rate: 0.08 },
    { limit: Infinity, rate: 0.10 }
  ],
  additional: [
    { limit: 6055070, rate: 0.08 },
    { limit: Infinity, rate: 0.10 }
  ],
  immigrant: [
    { limit: 1978745, rate: 0.00 },
    { limit: 6055070, rate: 0.005 },
    { limit: 20183565, rate: 0.08 },
    { limit: Infinity, rate: 0.10 }
  ]
};

// Translations Dictionary for Dynamic UI Elements
const TRANSLATIONS = {
  he: {
    bracketFree: "פטור ממס",
    bracketText: "מדרגה של {rate}% (בין {min} ל-{max} ₪)",
    bracketAbove: "מדרגה של {rate}% (מעל {min} ₪)",
    taxCalculated: "מס רכישה צפוי",
    nis: "₪",
    sending: "שולח הודעה...",
    pleaseWait: "אנא המתן רגע.",
    successTitle: "ההודעה נשלחה בהצלחה!",
    successSub: "תודה, עו״ד אלגרבלי יחזור אליך בהקדם האפשרי.",
    close: "סגור"
  },
  en: {
    bracketFree: "Tax Exempt",
    bracketText: "{rate}% Bracket (between {min} and {max} NIS)",
    bracketAbove: "{rate}% Bracket (above {min} NIS)",
    taxCalculated: "Estimated Purchase Tax",
    nis: "NIS",
    sending: "Sending message...",
    pleaseWait: "Please wait a moment.",
    successTitle: "Message Sent Successfully!",
    successSub: "Thank you. Adv. Elgarably will contact you shortly.",
    close: "Close"
  }
};

// ==========================================================================
// Initialization
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  // Detect language from URL path (SEO-friendly)
  if (window.location.pathname.includes('/en/')) {
    currentLanguage = 'en';
  } else {
    currentLanguage = 'he';
  }
  localStorage.setItem('elgarably_lang', currentLanguage);
  setLanguage(currentLanguage);

  // Preserve location hashes when toggling languages
  document.querySelectorAll('.lang-btn-he').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const hash = window.location.hash || '';
      window.location.href = btn.getAttribute('href') + hash;
    });
  });
  document.querySelectorAll('.lang-btn-en').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const hash = window.location.hash || '';
      window.location.href = btn.getAttribute('href') + hash;
    });
  });

  // Initialize Header Scroll Observer
  initHeaderScroll();

  // Initialize Mobile Navigation Toggler
  initMobileNav();

  // Initialize the "Calculators" nav dropdown (hover + click + keyboard)
  initNavDropdown();

  // Initialize Scroll Counters & Reveals
  initScrollAnimations();

  // Initial Calculation (guarded for elements presence)
  if (document.getElementById('calc-price-text')) {
    calculatePurchaseTax();
  }
  if (document.getElementById('yield-price-text')) {
    calculateYield();
  }

  // Initialize Articles Slider Navigation Arrows state
  const sliderContainer = document.getElementById('articles-slider-container');
  if (sliderContainer) {
    sliderContainer.addEventListener('scroll', updateSliderArrows, { passive: true });
    updateSliderArrows();
    window.addEventListener('resize', updateSliderArrows, { passive: true });
  }
});

// ==========================================================================
// Bilingual System
// ==========================================================================
function setLanguage(lang) {
  currentLanguage = lang;
  localStorage.setItem('elgarably_lang', lang);

  const body = document.getElementById('body-element');
  const htmlDoc = document.documentElement;

  if (body) {
    if (lang === 'he') {
      body.className = 'lang-he';
      htmlDoc.setAttribute('lang', 'he');
      htmlDoc.setAttribute('dir', 'rtl');
    } else {
      body.className = 'lang-en';
      htmlDoc.setAttribute('lang', 'en');
      htmlDoc.setAttribute('dir', 'ltr');
    }
  }

  const toggleHe = document.getElementById('lang-toggle-he');
  const toggleEn = document.getElementById('lang-toggle-en');
  if (toggleHe && toggleEn) {
    if (lang === 'he') {
      toggleHe.classList.add('active');
      toggleEn.classList.remove('active');
    } else {
      toggleEn.classList.add('active');
      toggleHe.classList.remove('active');
    }
  }

  // Recalculate Purchase Tax to redraw breakdown in active language (guarded)
  if (document.getElementById('calc-price-text')) {
    calculatePurchaseTax();
  }
  if (document.getElementById('yield-price-text')) {
    calculateYield();
  }
  if (document.getElementById('articles-slider-container')) {
    updateSliderArrows();
  }
  // Re-render the transaction-cost calculators (js/calculators.js) in the active language
  if (typeof renderActiveCalculator === 'function') {
    renderActiveCalculator();
  }
}

// ==========================================================================
// Navigation & Header Scroll effects
// ==========================================================================
function initHeaderScroll() {
  const header = document.getElementById('header');
  if (!header) return;

  const hasHero = document.getElementById('hero') !== null;

  if (!hasHero) {
    header.classList.add('header-scrolled');
    return;
  }
  
  const handleScroll = () => {
    if (window.scrollY > 50) {
      header.classList.add('header-scrolled');
    } else {
      header.classList.remove('header-scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll);
  handleScroll(); // Trigger immediately to check initial state
}

// Collapse every open nav dropdown and reset its ARIA state
function closeAllNavDropdowns() {
  document.querySelectorAll('.nav-item-dropdown.open').forEach(item => {
    item.classList.remove('open');
    const toggle = item.querySelector('.nav-dropdown-toggle');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
  });
}

function initMobileNav() {
  const hamburger = document.getElementById('mobile-nav-toggle');
  const menu = document.getElementById('nav-menu');
  if (!hamburger || !menu) return;

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    const isOpen = menu.classList.toggle('active');
    // Reset any expanded sub-menu whenever the drawer is closed
    if (!isOpen) closeAllNavDropdowns();
  });

  // Close the drawer when an actual navigation link is clicked.
  // The dropdown toggle is a <button>, so it is intentionally excluded here.
  menu.querySelectorAll('a.nav-link, .nav-dropdown-link').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      menu.classList.remove('active');
      closeAllNavDropdowns();
    });
  });
}

// Accessible dropdown for the "מחשבונים / Calculators" menu.
// Desktop reveals the panel on hover/focus via CSS; this adds click + keyboard
// support and powers the inline accordion inside the mobile drawer.
function initNavDropdown() {
  const dropdowns = document.querySelectorAll('.nav-item-dropdown');
  if (!dropdowns.length) return;

  dropdowns.forEach(item => {
    const toggle = item.querySelector('.nav-dropdown-toggle');
    if (!toggle) return;

    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const willOpen = !item.classList.contains('open');
      closeAllNavDropdowns(); // keep only one panel open at a time
      item.classList.toggle('open', willOpen);
      toggle.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
    });
  });

  // Click outside any dropdown closes the open panel
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-item-dropdown')) closeAllNavDropdowns();
  });

  // Escape closes the open panel and returns focus to its toggle
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    const open = document.querySelector('.nav-item-dropdown.open');
    if (!open) return;
    closeAllNavDropdowns();
    const toggle = open.querySelector('.nav-dropdown-toggle');
    if (toggle) toggle.focus();
  });
}

// ==========================================================================
// Stats count-up animation & Scroll reveal
// ==========================================================================
function initScrollAnimations() {
  const statNumbers = document.querySelectorAll('.stat-number');
  
  const options = {
    threshold: 0.5,
    rootMargin: '0px 0px -50px 0px'
  };

  const countUp = (element) => {
    const target = parseInt(element.getAttribute('data-target'), 10);
    const duration = 2000; // 2 seconds animation
    const startTime = performance.now();

    const updateCount = (currentTime) => {
      const elapsedTime = currentTime - startTime;
      const progress = Math.min(elapsedTime / duration, 1);
      
      // Ease out cubic function
      const easeProgress = 1 - Math.pow(1 - progress, 3);
      const currentValue = Math.floor(easeProgress * target);

      // Formatting details (+ or % symbol)
      if (element.id === 'stat-years') {
        element.textContent = currentValue + '+';
      } else if (element.id === 'stat-deals') {
        element.textContent = currentValue.toLocaleString() + '+';
      } else if (element.id === 'stat-tax') {
        element.textContent = currentValue + 'M+';
      } else if (element.id === 'stat-rate') {
        element.textContent = currentValue + '%';
      } else {
        element.textContent = currentValue.toLocaleString();
      }

      if (progress < 1) {
        requestAnimationFrame(updateCount);
      } else {
        // Set exact target value at the end
        if (element.id === 'stat-years') {
          element.textContent = target + '+';
        } else if (element.id === 'stat-deals') {
          element.textContent = target.toLocaleString() + '+';
        } else if (element.id === 'stat-tax') {
          element.textContent = target + 'M+';
        } else if (element.id === 'stat-rate') {
          element.textContent = target + '%';
        }
      }
    };

    requestAnimationFrame(updateCount);
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        countUp(entry.target);
        observer.unobserve(entry.target); // Trigger count up only once
      }
    });
  }, options);

  statNumbers.forEach(stat => {
    observer.observe(stat);
  });
}
// ==========================================================================
// Interactive Purchase Tax Calculator
// ==========================================================================
function setCalcPropertyType(type) {
  currentPropertyType = type;

  // Update active state across all four cards
  const cards = {
    single: document.getElementById('radio-single-home'),
    additional: document.getElementById('radio-additional-home'),
    immigrant: document.getElementById('radio-immigrant-home'),
    disabled: document.getElementById('radio-disabled-home')
  };
  Object.values(cards).forEach(card => card && card.classList.remove('active'));
  if (cards[type]) cards[type].classList.add('active');

  const radioIds = { single: 'prop-single', additional: 'prop-additional', immigrant: 'prop-immigrant', disabled: 'prop-disabled' };
  const radio = document.getElementById(radioIds[type]);
  if (radio) radio.checked = true;

  // Reveal the disabled/blind sub-type toggle and manage the gift checkbox.
  // The "gift from a relative" relief is a separate track and does not stack
  // with the disabled relief, so we disable it while the disabled track is active.
  const subTypeBox = document.getElementById('calc-disabled-subtype');
  const giftLabel = document.getElementById('calc-gift-label');
  const giftCheckbox = document.getElementById('calc-is-gift');

  if (type === 'disabled') {
    if (subTypeBox) subTypeBox.classList.add('open');
    if (giftCheckbox) { giftCheckbox.checked = false; giftCheckbox.disabled = true; }
    if (giftLabel) giftLabel.classList.add('is-disabled');
    isGiftProperty = false;
  } else {
    if (subTypeBox) subTypeBox.classList.remove('open');
    if (giftCheckbox) giftCheckbox.disabled = false;
    if (giftLabel) giftLabel.classList.remove('is-disabled');
  }

  calculatePurchaseTax();
}

// Sub-type toggle inside the disabled/blind track: single home vs additional home
function setDisabledSubType(sub) {
  currentDisabledSubType = sub;
  const singleBtn = document.getElementById('subtype-single');
  const additionalBtn = document.getElementById('subtype-additional');
  if (singleBtn) singleBtn.classList.toggle('active', sub === 'single');
  if (additionalBtn) additionalBtn.classList.toggle('active', sub === 'additional');
  calculatePurchaseTax();
}

// Disabled / Blind purchase tax (Regulation 11) — returns { total, rows }
// Single home up to 2.5M: exempt up to the ceiling, then 0.5% on the balance.
// Single home above 2.5M, OR any additional home: flat 0.5% on the WHOLE value.
function computeDisabledBreakdown(price, subType) {
  const rows = [];
  let total = 0;

  if (subType === 'single' && price <= DISABLED_FLAT_THRESHOLD) {
    const exemptPart = Math.min(price, DISABLED_EXEMPT_CEILING);
    rows.push({ kind: 'exempt', from: 0, to: DISABLED_EXEMPT_CEILING, rate: 0, taxable: exemptPart, tax: 0 });
    if (price > DISABLED_EXEMPT_CEILING) {
      const taxable = price - DISABLED_EXEMPT_CEILING;
      const tax = Math.round(taxable * DISABLED_RATE);
      total += tax;
      rows.push({ kind: 'partial', from: DISABLED_EXEMPT_CEILING, to: DISABLED_FLAT_THRESHOLD, rate: DISABLED_RATE, taxable: taxable, tax: tax });
    }
  } else {
    const tax = Math.round(price * DISABLED_RATE);
    total += tax;
    rows.push({ kind: 'flat', from: 0, to: Infinity, rate: DISABLED_RATE, taxable: price, tax: tax, aboveThreshold: (subType === 'single') });
  }

  return { total: total, rows: rows };
}

// Render the disabled/blind breakdown into the on-page results list
function renderDisabledBreakdown(price, listContainer) {
  const isHe = currentLanguage === 'he';
  const fmt = n => isHe ? `${n.toLocaleString()} ₪` : `₪ ${n.toLocaleString()}`;
  const ceiling = DISABLED_EXEMPT_CEILING.toLocaleString();
  const threshold = DISABLED_FLAT_THRESHOLD.toLocaleString();

  const { total, rows } = computeDisabledBreakdown(price, currentDisabledSubType);

  rows.forEach(r => {
    const li = document.createElement('li');
    li.className = 'breakdown-item';
    const textSpan = document.createElement('span');
    const valueSpan = document.createElement('span');

    if (r.kind === 'exempt') {
      textSpan.textContent = isHe
        ? `פטור מלא ממס רכישה (עד ${ceiling} ₪)`
        : `Full purchase-tax exemption (up to ${ceiling} NIS)`;
      valueSpan.textContent = isHe ? 'פטור ממס' : 'Tax Exempt';
      valueSpan.style.color = '#5CB85C';
      valueSpan.style.fontWeight = '600';
    } else if (r.kind === 'partial') {
      textSpan.textContent = isHe
        ? `0.5% על היתרה (מעל ${ceiling} ₪)`
        : `0.5% on the balance (above ${ceiling} NIS)`;
      valueSpan.textContent = fmt(r.tax);
    } else { // flat
      textSpan.textContent = r.aboveThreshold
        ? (isHe ? `0.5% על מלוא שווי הרכישה (דירה יחידה מעל ${threshold} ₪)` : `0.5% on the full purchase value (single home above ${threshold} NIS)`)
        : (isHe ? '0.5% על מלוא שווי הרכישה' : '0.5% on the full purchase value');
      valueSpan.textContent = fmt(r.tax);
    }

    li.appendChild(textSpan);
    li.appendChild(valueSpan);
    listContainer.appendChild(li);
  });

  const totalLi = document.createElement('li');
  totalLi.className = 'breakdown-item total';
  const totalTextSpan = document.createElement('span');
  totalTextSpan.textContent = isHe ? 'סה"כ מס לתשלום:' : 'Total Tax Due:';
  const totalValueSpan = document.createElement('span');
  totalValueSpan.textContent = fmt(total);
  totalLi.appendChild(totalTextSpan);
  totalLi.appendChild(totalValueSpan);
  listContainer.appendChild(totalLi);

  const bigNumber = document.getElementById('tax-result-value');
  if (bigNumber) {
    bigNumber.innerHTML = isHe
      ? `${total.toLocaleString()}<span>₪</span>`
      : `<span>₪</span>${total.toLocaleString()}`;
  }
}

function handleGiftCheckboxChange(checkbox) {
  isGiftProperty = checkbox.checked;
  calculatePurchaseTax();
}

function handlePriceRangeInput(slider) {
  const value = parseInt(slider.value, 10);
  document.getElementById('calc-price-text').value = value.toLocaleString();
  calculatePurchaseTax();
}

function handlePriceTextInput(textInput) {
  // Extract digits only
  let valueStr = textInput.value.replace(/\D/g, '');
  let value = parseInt(valueStr, 10);
  
  if (isNaN(value)) {
    value = 0;
  }

  // Cap value for sanity check
  if (value > 50000000) value = 50000000;
  
  textInput.value = value.toLocaleString();
  
  // Sync slider
  const slider = document.getElementById('calc-price-range');
  if (value >= slider.min && value <= slider.max) {
    slider.value = value;
  } else if (value < slider.min) {
    slider.value = slider.min;
  } else if (value > slider.max) {
    slider.value = slider.max;
  }
  
  calculatePurchaseTax();
}

function calculatePurchaseTax() {
  const priceEl = document.getElementById('calc-price-text');
  if (!priceEl) return;
  const priceInput = priceEl.value;
  const price = parseInt(priceInput.replace(/\D/g, ''), 10) || 0;

  const listContainer = document.getElementById('tax-breakdown-list');
  if (!listContainer) return;
  listContainer.innerHTML = '';

  // Disabled / Blind track (Regulation 11) uses its own non-marginal logic
  if (currentPropertyType === 'disabled') {
    renderDisabledBreakdown(price, listContainer);
    return;
  }

  const brackets = TAX_BRACKETS[currentPropertyType];
  let totalTax = 0;
  let remainingPrice = price;
  let prevLimit = 0;
  
  const langText = TRANSLATIONS[currentLanguage];
  
  brackets.forEach(bracket => {
    if (prevLimit >= price) return; // Price is fully calculated in previous brackets
    
    const bracketSize = bracket.limit - prevLimit;
    const taxableAmount = Math.min(remainingPrice, bracketSize);
    const taxInBracket = Math.round((taxableAmount * bracket.rate) / (isGiftProperty ? 3 : 1));
    totalTax += taxInBracket;
    
    // Formatting breakdown item description text
    let description = '';
    const ratePercent = (bracket.rate * 100).toFixed((bracket.rate * 100) % 1 === 0 ? 0 : 1);
    
    if (bracket.limit === Infinity) {
      description = langText.bracketAbove
        .replace('{rate}', ratePercent)
        .replace('{min}', prevLimit.toLocaleString());
    } else {
      description = langText.bracketText
        .replace('{rate}', ratePercent)
        .replace('{min}', prevLimit.toLocaleString())
        .replace('{max}', bracket.limit.toLocaleString());
    }
    
    // Create HTML List element
    const li = document.createElement('li');
    li.className = 'breakdown-item';
    
    const textSpan = document.createElement('span');
    textSpan.textContent = description;
    
    const valueSpan = document.createElement('span');
    if (bracket.rate === 0) {
      valueSpan.textContent = langText.bracketFree;
      valueSpan.style.color = '#5CB85C';
      valueSpan.style.fontWeight = '600';
    } else {
      if (currentLanguage === 'he') {
        valueSpan.textContent = `${taxInBracket.toLocaleString()} ₪`;
      } else {
        valueSpan.textContent = `₪ ${taxInBracket.toLocaleString()}`;
      }
    }
    
    li.appendChild(textSpan);
    li.appendChild(valueSpan);
    
    listContainer.appendChild(li);
    
    remainingPrice -= taxableAmount;
    prevLimit = bracket.limit;
  });
  
  // Append Grand Total Row
  const totalLi = document.createElement('li');
  totalLi.className = 'breakdown-item total';
  
  const totalTextSpan = document.createElement('span');
  totalTextSpan.textContent = currentLanguage === 'he' ? 'סה"כ מס לתשלום:' : 'Total Tax Due:';
  
  const totalValueSpan = document.createElement('span');
  if (currentLanguage === 'he') {
    totalValueSpan.textContent = `${totalTax.toLocaleString()} ₪`;
  } else {
    totalValueSpan.textContent = `₪ ${totalTax.toLocaleString()}`;
  }
  
  totalLi.appendChild(totalTextSpan);
  totalLi.appendChild(totalValueSpan);
  listContainer.appendChild(totalLi);
  
  // Update Main Big Number
  if (currentLanguage === 'he') {
    document.getElementById('tax-result-value').innerHTML = `${totalTax.toLocaleString()}<span>₪</span>`;
  } else {
    document.getElementById('tax-result-value').innerHTML = `<span>₪</span>${totalTax.toLocaleString()}`;
  }
}

// ==========================================================================
// Printable Branded Tax Report
// ==========================================================================

// Pure calculation helper (no DOM) - returns full bracket breakdown
function computeTaxBreakdown(price, type, gift) {
  // Disabled / Blind track has its own (non-marginal) computation
  if (type === 'disabled') {
    return computeDisabledBreakdown(price, currentDisabledSubType);
  }

  const brackets = TAX_BRACKETS[type];
  const rows = [];
  let total = 0;
  let remaining = price;
  let prevLimit = 0;

  brackets.forEach(bracket => {
    if (prevLimit >= price) return;
    const bracketSize = bracket.limit - prevLimit;
    const taxable = Math.min(remaining, bracketSize);
    const tax = Math.round((taxable * bracket.rate) / (gift ? 3 : 1));
    total += tax;
    rows.push({ from: prevLimit, to: bracket.limit, rate: bracket.rate, taxable: taxable, tax: tax });
    remaining -= taxable;
    prevLimit = bracket.limit;
  });

  return { total: total, rows: rows };
}

function formatRatePercent(rate) {
  const pct = rate * 100;
  return pct % 1 === 0 ? pct.toFixed(0) : pct.toFixed(1);
}

function buildTaxReportHTML(opts) {
  const isHe = opts.lang === 'he';
  const fmt = n => isHe ? `${n.toLocaleString()} ₪` : `₪ ${n.toLocaleString()}`;
  const INF = '∞';

  const L = isHe ? {
    docTitle: 'דוח חישוב מס רכישה — משרד עו״ד אלירם אלגרבלי',
    firmName: 'משרד עו״ד אלירם אלגרבלי',
    firmTag: 'מקרקעין · מיסוי מקרקעין · ירושות וצוואות',
    reportTitle: 'דוח חישוב מס רכישה',
    reportSub: 'מדרגות מס רכישה בתוקף לתקופה שבין 16.1.24 ל-15.1.27',
    metaPrice: 'שווי הנכס הנרכש',
    metaType: 'סוג הנכס',
    metaDate: 'תאריך הפקת הדוח',
    metaRate: 'שיעור המס האפקטיבי',
    totalLabel: 'מס הרכישה הצפוי בעסקה',
    breakdownTitle: 'פירוט החישוב לפי מדרגות',
    colFrom: 'מסכום', colTo: 'עד סכום', colRate: 'שיעור המס', colTaxable: 'הסכום במדרגה', colTax: 'מס לתשלום',
    exempt: 'פטור ממס',
    totalRow: 'סה״כ מס רכישה לתשלום',
    typeSingle: 'דירת מגורים יחידה',
    typeAdditional: 'דירה נוספת / דירה להשקעה',
    typeImmigrant: 'עולה חדש (תקנה 12 לתקנות מיסוי מקרקעין)',
    typeDisabledSingle: 'נכה / עיוור — דירה יחידה (תקנה 11)',
    typeDisabledAdditional: 'נכה / עיוור — דירה נוספת (תקנה 11)',
    disabledTitle: 'הקלה לנכה / עיוור (תקנה 11): ',
    disabledNote: 'מכירת זכות במקרקעין לנכה, עיוור, נפגע או בן משפחה של חייל שנספה — לשם מגוריו — חייבת במס רכישה בשיעור 0.5%. בדירה יחידה ששוויה עד 2,500,000 ₪ יחול פטור מלא עד 1,978,745 ₪ ו-0.5% על היתרה; בדירה יחידה מעל סכום זה, וכן בדירה נוספת המשמשת למגוריו — 0.5% על מלוא שווי הרכישה. ההטבה ניתנת עד פעמיים בחיי הזכאי, מותנית בכך שהדירה תשמש למגוריו (ולא כהשקעה), ומוגשת באמצעות טופס 2973.',
    giftNote: 'החישוב בוצע עבור העברה ללא תמורה מקרוב (סכומי המס משקפים שליש ממס הרכישה הרגיל).',
    savingsTitle: 'לתשומת ליבך — משפרי דיור:',
    savings: (single, saved) => `בהתאם לסעיף 9(ג1ג)(2) לחוק מיסוי מקרקעין (שבח ורכישה), התשכ״ג-1963, רוכש המתחייב במסגרת הדיווח לרשות המיסים למכור את דירתו הקיימת בתוך 18 חודשים ממועד רכישת הדירה החדשה, יחויב במס רכישה לפי מדרגות דירה יחידה. במקרה כזה יעמוד מס הרכישה על <strong>${single}</strong> בלבד — חיסכון פוטנציאלי של <strong>${saved}</strong>.`,
    refTitle: 'מדרגות מס רכישה — טבלאות מלאות (16.1.24 – 15.1.27)',
    refSingle: 'דירה יחידה', refAdditional: 'דירה נוספת',
    contact: 'טל׳: 08-6206666 · ארה״ב: +1 (424) 367-8863 · office@madrich.co.il',
    disclaimer: 'הדוח מבוסס על מדרגות מס הרכישה המעודכנות לדירות מגורים והופק באמצעות הסימולטור שבאתר המשרד. מדובר בסימולציה ראשונית בלבד, שאינה מהווה ייעוץ משפטי או תחליף לתכנון מס פרטני על ידי עורך דין מקרקעין מוסמך.',
    btnPrint: 'הדפסה / שמירה כ-PDF', btnClose: 'סגירה'
  } : {
    docTitle: 'Purchase Tax Calculation Report — Elgrably Law Firm',
    firmName: 'ELGRABLY LAW FIRM',
    firmTag: 'Real Estate · Property Taxation · Wills & Inheritance',
    reportTitle: 'Purchase Tax Calculation Report',
    reportSub: 'Purchase tax brackets in effect for the period 16.1.24 – 15.1.27',
    metaPrice: 'Property Value',
    metaType: 'Property Type',
    metaDate: 'Report Date',
    metaRate: 'Effective Tax Rate',
    totalLabel: 'Estimated Purchase Tax',
    breakdownTitle: 'Bracket-by-Bracket Calculation',
    colFrom: 'From', colTo: 'Up To', colRate: 'Tax Rate', colTaxable: 'Amount in Bracket', colTax: 'Tax Due',
    exempt: 'Tax Exempt',
    totalRow: 'Total Purchase Tax Due',
    typeSingle: 'Single Residential Home',
    typeAdditional: 'Additional / Investment Property',
    typeImmigrant: 'New Immigrant (Regulation 12)',
    typeDisabledSingle: 'Disabled / Blind — Single Home (Reg. 11)',
    typeDisabledAdditional: 'Disabled / Blind — Additional Home (Reg. 11)',
    disabledTitle: 'Disabled / Blind relief (Regulation 11): ',
    disabledNote: 'A sale of real estate to a disabled person, a blind person, a victim (as defined by law), or a family member of a fallen soldier — for their own residence — is taxed at 0.5%. For a single home worth up to NIS 2,500,000, the first NIS 1,978,745 is fully exempt and 0.5% applies to the balance; for a single home above that amount, and for an additional home used as their residence, 0.5% applies to the entire purchase value. The benefit may be used up to twice in the beneficiary\'s lifetime, requires that the home serve as their residence (not an investment), and is claimed using Form 2973.',
    giftNote: 'Calculated as a transfer without consideration from a relative (tax amounts reflect one-third of the standard purchase tax).',
    savingsTitle: 'Note for Home Upgraders:',
    savings: (single, saved) => `Under Section 9(c1c)(2) of the Real Estate Taxation Law, 1963, a purchaser who commits — when filing the self-assessment with the Tax Authority — to sell their existing home within 18 months of purchasing the new one, is taxed at the single-home brackets. In that case, the purchase tax would be only <strong>${single}</strong> — a potential saving of <strong>${saved}</strong>.`,
    refTitle: 'Full Purchase Tax Bracket Tables (16.1.24 – 15.1.27)',
    refSingle: 'Single Home', refAdditional: 'Additional Home',
    contact: 'Tel: 08-6206666 · US: +1 (424) 367-8863 · office@madrich.co.il',
    disclaimer: 'This report is based on the updated residential purchase tax brackets and was generated by the simulator on the firm\'s website. It is a preliminary simulation only and does not constitute legal advice or replace individual tax planning by a qualified real estate attorney.',
    btnPrint: 'Print / Save as PDF', btnClose: 'Close'
  };

  const typeLabels = { single: L.typeSingle, additional: L.typeAdditional, immigrant: L.typeImmigrant };
  const typeLabel = opts.type === 'disabled'
    ? (opts.disabledSubType === 'additional' ? L.typeDisabledAdditional : L.typeDisabledSingle)
    : (typeLabels[opts.type] || '');
  const effectiveRate = opts.price > 0 ? ((opts.breakdown.total / opts.price) * 100).toFixed(2) : '0.00';

  const breakdownRows = opts.breakdown.rows.map(r => `
      <tr>
        <td>${fmt(r.from)}</td>
        <td>${r.to === Infinity ? INF : fmt(r.to)}</td>
        <td>${formatRatePercent(r.rate)}%</td>
        <td>${fmt(r.taxable)}</td>
        <td>${r.tax === 0 ? `<span class="exempt">${L.exempt}</span>` : fmt(r.tax)}</td>
      </tr>`).join('');

  const refRows = type => {
    let prev = 0;
    return TAX_BRACKETS[type].map(b => {
      const row = `<tr><td>${fmt(prev)}</td><td>${b.limit === Infinity ? INF : fmt(b.limit)}</td><td>${formatRatePercent(b.rate)}%</td></tr>`;
      prev = b.limit;
      return row;
    }).join('');
  };

  const giftBlock = opts.gift
    ? `<div class="callout"><strong>${isHe ? 'העברה ללא תמורה: ' : 'Gift Transfer: '}</strong>${L.giftNote}</div>`
    : '';

  const savingsBlock = (opts.type === 'additional' && opts.savings > 0)
    ? `<div class="callout gold"><strong>${L.savingsTitle}</strong> ${L.savings(fmt(opts.singleTotal), fmt(opts.savings))}</div>`
    : '';

  const disabledBlock = (opts.type === 'disabled')
    ? `<div class="callout"><strong>${L.disabledTitle}</strong>${L.disabledNote}</div>`
    : '';

  return `<!DOCTYPE html>
<html lang="${opts.lang}" dir="${isHe ? 'rtl' : 'ltr'}">
<head>
<meta charset="UTF-8">
<title>${L.docTitle}</title>
<link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700;800&family=Cinzel:wght@600;700&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  html, body { background: #FFFFFF; }
  body { font-family: 'Assistant', sans-serif; color: #1C2541; }
  .toolbar { position: fixed; top: 0; left: 0; right: 0; display: flex; justify-content: center; gap: 10px; padding: 12px; background: #0A1128; z-index: 10; }
  .toolbar button { font-family: 'Assistant', sans-serif; font-size: 15px; font-weight: 600; padding: 8px 22px; border-radius: 4px; cursor: pointer; border: 1px solid #C5A880; }
  .toolbar .primary { background: #C5A880; color: #0A1128; }
  .toolbar .secondary { background: transparent; color: #C5A880; }
  .screen-offset { height: 64px; }
  .page { width: 210mm; margin: 0 auto; padding: 0 14mm 8mm; }
  .gold-rule { height: 5px; background: linear-gradient(90deg, #8F724C, #E5C494, #8F724C); }
  .report-header { text-align: center; padding: 9mm 0 5mm; border-bottom: 1px solid rgba(197,168,128,.5); }
  .report-header img { height: 64px; }
  .firm-name { font-family: ${isHe ? "'Assistant', sans-serif" : "'Cinzel', serif"}; font-size: 15px; font-weight: 700; letter-spacing: ${isHe ? '.05em' : '.3em'}; color: #0A1128; margin-top: 3mm; }
  .firm-tag { font-size: 10.5px; color: #8F724C; letter-spacing: .12em; margin-top: 1mm; }
  h1 { font-size: 24px; font-weight: 800; color: #0A1128; text-align: center; margin-top: 7mm; }
  .report-sub { text-align: center; color: #6C7A89; font-size: 11.5px; margin-top: 1.5mm; }
  .meta-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 4mm; margin-top: 7mm; }
  .meta-card { border: 1px solid rgba(197,168,128,.45); border-radius: 6px; padding: 3.5mm 2mm; text-align: center; background: #FCFBF9; }
  .meta-label { font-size: 9.5px; font-weight: 600; color: #8F724C; letter-spacing: .06em; }
  .meta-value { font-size: 13.5px; font-weight: 700; color: #0A1128; margin-top: 1.5mm; }
  .total-band { margin-top: 6mm; background: linear-gradient(135deg, #0A1128, #101F42); border-radius: 8px; padding: 5.5mm 8mm; display: flex; align-items: center; justify-content: space-between; }
  .total-band .label { color: #F4F5F7; font-size: 14px; font-weight: 600; }
  .total-band .amount { color: #E5C494; font-size: 28px; font-weight: 800; }
  h2 { font-size: 13.5px; font-weight: 700; color: #0A1128; border-inline-start: 3px solid #C5A880; padding-inline-start: 3mm; margin: 7mm 0 3mm; }
  table { width: 100%; border-collapse: collapse; font-size: 11.5px; }
  th { background: #0A1128; color: #E5C494; font-weight: 600; padding: 2.6mm 2mm; text-align: center; }
  td { padding: 2.4mm 2mm; text-align: center; border-bottom: 1px solid #ECECEC; }
  tbody tr:nth-child(even) td { background: #FAF8F5; }
  .exempt { color: #3D8B40; font-weight: 700; }
  tr.total-row td { background: rgba(197,168,128,.14); border-top: 2px solid #C5A880; border-bottom: none; font-weight: 800; font-size: 12.5px; color: #0A1128; }
  .callout { margin-top: 4.5mm; border: 1px solid rgba(197,168,128,.5); border-radius: 6px; background: rgba(197,168,128,.08); padding: 3.5mm 4.5mm; font-size: 11px; line-height: 1.6; }
  .callout.gold { background: rgba(197,168,128,.16); }
  .callout strong { color: #8F724C; }
  .ref-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6mm; }
  .ref-grid h3 { font-size: 11.5px; font-weight: 700; color: #8F724C; margin-bottom: 1.5mm; text-align: center; }
  .report-footer { margin-top: 8mm; border-top: 1px solid rgba(197,168,128,.5); padding-top: 3.5mm; text-align: center; }
  .footer-firm { font-size: 11px; font-weight: 700; color: #0A1128; }
  .footer-contact { font-size: 10px; color: #6C7A89; margin-top: 1mm; direction: ltr; }
  .footer-disclaimer { font-size: 8.5px; color: #9AA3AD; line-height: 1.55; margin-top: 2mm; text-align: justify; }
  @page { size: A4; margin: 0; }
  @media print {
    .toolbar, .screen-offset { display: none; }
    .page { width: 100%; }
  }
</style>
</head>
<body>
  <div class="toolbar">
    <button class="primary" onclick="window.print()">${L.btnPrint}</button>
    <button class="secondary" onclick="window.close()">${L.btnClose}</button>
  </div>
  <div class="screen-offset"></div>
  <div class="gold-rule"></div>
  <div class="page">
    <div class="report-header">
      <img src="${opts.logoUrl}" alt="${L.firmName}">
      <div class="firm-name">${L.firmName}</div>
      <div class="firm-tag">${L.firmTag}</div>
    </div>

    <h1>${L.reportTitle}</h1>
    <div class="report-sub">${L.reportSub}</div>

    <div class="meta-grid">
      <div class="meta-card"><div class="meta-label">${L.metaPrice}</div><div class="meta-value">${fmt(opts.price)}</div></div>
      <div class="meta-card"><div class="meta-label">${L.metaType}</div><div class="meta-value">${typeLabel}</div></div>
      <div class="meta-card"><div class="meta-label">${L.metaRate}</div><div class="meta-value">${effectiveRate}%</div></div>
      <div class="meta-card"><div class="meta-label">${L.metaDate}</div><div class="meta-value">${opts.dateStr}</div></div>
    </div>

    <div class="total-band">
      <span class="label">${L.totalLabel}</span>
      <span class="amount">${fmt(opts.breakdown.total)}</span>
    </div>

    <h2>${L.breakdownTitle}</h2>
    <table>
      <thead>
        <tr><th>${L.colFrom}</th><th>${L.colTo}</th><th>${L.colRate}</th><th>${L.colTaxable}</th><th>${L.colTax}</th></tr>
      </thead>
      <tbody>
        ${breakdownRows}
        <tr class="total-row"><td colspan="4">${L.totalRow}</td><td>${fmt(opts.breakdown.total)}</td></tr>
      </tbody>
    </table>

    ${giftBlock}
    ${savingsBlock}
    ${disabledBlock}

    <h2>${L.refTitle}</h2>
    <div class="ref-grid">
      <div>
        <h3>${L.refSingle}</h3>
        <table>
          <thead><tr><th>${L.colFrom}</th><th>${L.colTo}</th><th>${L.colRate}</th></tr></thead>
          <tbody>${refRows('single')}</tbody>
        </table>
      </div>
      <div>
        <h3>${L.refAdditional}</h3>
        <table>
          <thead><tr><th>${L.colFrom}</th><th>${L.colTo}</th><th>${L.colRate}</th></tr></thead>
          <tbody>${refRows('additional')}</tbody>
        </table>
      </div>
    </div>

    <div class="report-footer">
      <div class="footer-firm">${L.firmName}</div>
      <div class="footer-contact">${L.contact}</div>
      <div class="footer-disclaimer">* ${L.disclaimer}</div>
    </div>
  </div>
</body>
</html>`;
}

function printTaxReport() {
  const priceEl = document.getElementById('calc-price-text');
  if (!priceEl) return;
  const price = parseInt(priceEl.value.replace(/\D/g, ''), 10) || 0;

  const breakdown = computeTaxBreakdown(price, currentPropertyType, isGiftProperty);

  // Potential single-home tax for the "home upgrader" savings note
  const singleTotal = computeTaxBreakdown(price, 'single', isGiftProperty).total;
  const savings = breakdown.total - singleTotal;

  // Resolve logo as absolute URL (works from / and /en/ alike)
  const logoUrl = new URL(
    (window.location.pathname.includes('/en/') ? '../' : '') + 'assets/logo.png',
    window.location.href
  ).href;

  const dateStr = new Date().toLocaleDateString(currentLanguage === 'he' ? 'he-IL' : 'en-GB');

  const html = buildTaxReportHTML({
    lang: currentLanguage,
    price: price,
    type: currentPropertyType,
    disabledSubType: currentDisabledSubType,
    gift: isGiftProperty,
    breakdown: breakdown,
    singleTotal: singleTotal,
    savings: savings,
    logoUrl: logoUrl,
    dateStr: dateStr
  });

  const reportWindow = window.open('', '_blank');
  if (!reportWindow) {
    alert(currentLanguage === 'he'
      ? 'לא ניתן לפתוח את חלון הדוח. אנא אפשר חלונות קופצים עבור אתר זה.'
      : 'Could not open the report window. Please allow pop-ups for this site.');
    return;
  }
  reportWindow.document.write(html);
  reportWindow.document.close();

  // Trigger the print dialog once assets have loaded
  reportWindow.addEventListener('load', function () {
    setTimeout(function () { reportWindow.focus(); reportWindow.print(); }, 400);
  });
}

// ==========================================================================
// Contact Form Submission (real delivery)
// ==========================================================================
// HOW LEADS ARE DELIVERED:
//   1) If FORM_ENDPOINT below is set to a Formspree URL, the form is submitted
//      via AJAX and the lead lands in the firm's inbox (the nice success
//      screen is preserved, no page reload).
//   2) If FORM_ENDPOINT is left empty, the form falls back to opening the
//      visitor's email app with all fields pre-filled, addressed to
//      CONTACT_EMAIL — so no lead is ever silently lost.
//
// To activate inbox delivery: create a free form at https://formspree.io,
// then paste its endpoint URL between the quotes below, e.g.
//   const FORM_ENDPOINT = "https://formspree.io/f/abcdwxyz";
const FORM_ENDPOINT = "";
const CONTACT_EMAIL = "office@madrich.co.il";

function showFormSuccess(title, sub, overlay, spinner, checkmark, titleEl, subEl, langText) {
  overlay.className = 'form-loading-overlay active success';
  spinner.style.display = 'none';
  checkmark.style.display = 'flex';
  titleEl.innerHTML = `<span>${title}</span>`;
  subEl.innerHTML = `<span>${sub}</span>`;

  const closeBtn = document.createElement('button');
  closeBtn.className = 'btn btn-outline';
  closeBtn.style.marginTop = '2rem';
  closeBtn.style.padding = '0.5rem 2rem';
  closeBtn.style.color = 'var(--color-primary)';
  closeBtn.style.borderColor = 'var(--color-accent-gold)';
  closeBtn.textContent = langText.close;
  closeBtn.onclick = () => {
    overlay.className = 'form-loading-overlay';
    document.getElementById('contact-form').reset();
    closeBtn.remove();
  };
  overlay.appendChild(closeBtn);
}

function handleFormSubmit(event) {
  event.preventDefault();

  const isHe = currentLanguage === 'he';
  const overlay = document.getElementById('form-loading-overlay');
  const spinner = document.getElementById('form-spinner');
  const checkmark = document.getElementById('form-success-checkmark');
  const title = document.getElementById('form-overlay-title');
  const sub = document.getElementById('form-overlay-sub');
  const langText = TRANSLATIONS[currentLanguage];

  // Collect the submitted values
  const form = document.getElementById('contact-form');
  const data = {
    name: (document.getElementById('form-name').value || '').trim(),
    phone: (document.getElementById('form-phone').value || '').trim(),
    email: (document.getElementById('form-email').value || '').trim(),
    subject: document.getElementById('form-subject').value || '',
    message: (document.getElementById('form-message').value || '').trim()
  };

  const subjectLabels = {
    'second-hand': isHe ? 'עסקת יד שנייה' : 'Second-Hand Transaction',
    'developer': isHe ? 'רכישה מקבלן' : 'Contractor Purchase',
    'urban-renewal': isHe ? 'התחדשות עירונית' : 'Urban Renewal',
    'tax-consultation': isHe ? 'ייעוץ מיסוי מקרקעין' : 'Real Estate Tax Planning',
    'other': isHe ? 'אחר' : 'Other'
  };
  const subjectLabel = subjectLabels[data.subject] || data.subject;

  // Show "sending" screen
  overlay.className = 'form-loading-overlay active';
  spinner.style.display = 'block';
  checkmark.style.display = 'none';
  title.innerHTML = `<span>${langText.sending}</span>`;
  sub.innerHTML = `<span>${langText.pleaseWait}</span>`;

  // Build a readable email body (used both as Formspree message and mailto fallback)
  const lines = isHe
    ? [`שם מלא: ${data.name}`, `טלפון: ${data.phone}`, `אימייל: ${data.email || '—'}`,
       `נושא: ${subjectLabel}`, '', 'תוכן הפנייה:', data.message]
    : [`Full name: ${data.name}`, `Phone: ${data.phone}`, `Email: ${data.email || '—'}`,
       `Topic: ${subjectLabel}`, '', 'Message:', data.message];
  const mailBody = lines.join('\n');
  const mailSubject = (isHe ? 'פנייה חדשה מהאתר' : 'New website inquiry') + ` – ${subjectLabel}`;

  const openMailFallback = () => {
    const href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(mailSubject)}&body=${encodeURIComponent(mailBody)}`;
    window.location.href = href;
    showFormSuccess(
      isHe ? 'תודה! פותחים את תוכנת הדוא״ל שלך' : 'Thank you! Opening your email app',
      isHe ? `אם החלון לא נפתח, אפשר לכתוב ישירות אל ${CONTACT_EMAIL}` : `If it didn't open, please email us directly at ${CONTACT_EMAIL}`,
      overlay, spinner, checkmark, title, sub, langText
    );
  };

  if (!FORM_ENDPOINT) {
    // No backend configured yet -> guaranteed-working email fallback
    setTimeout(openMailFallback, 600);
    return;
  }

  // Submit the lead to the configured endpoint (Formspree-compatible)
  fetch(FORM_ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
    body: JSON.stringify({
      name: data.name,
      phone: data.phone,
      email: data.email,
      topic: subjectLabel,
      message: data.message,
      _subject: mailSubject
    })
  })
    .then((res) => {
      if (!res.ok) throw new Error('Submission failed');
      showFormSuccess(langText.successTitle, langText.successSub,
        overlay, spinner, checkmark, title, sub, langText);
    })
    .catch(() => {
      // Network/endpoint error -> fall back to email so the lead is not lost
      openMailFallback();
    });
}

// ==========================================================================
// Interactive Yield Calculator Functions
// ==========================================================================
let isAdvancedYieldOpen = false;

function toggleAdvancedYieldExpenses() {
  const panel = document.getElementById('yield-advanced-expenses');
  const chevron = document.getElementById('yield-expenses-chevron');
  isAdvancedYieldOpen = !isAdvancedYieldOpen;
  
  if (isAdvancedYieldOpen) {
    panel.style.maxHeight = panel.scrollHeight + 'px';
    chevron.style.transform = 'rotate(180deg)';
  } else {
    panel.style.maxHeight = '0px';
    chevron.style.transform = 'rotate(0deg)';
  }
}

function handleYieldRangeInput(slider, type) {
  const value = parseInt(slider.value, 10);
  if (type === 'price') {
    document.getElementById('yield-price-text').value = value.toLocaleString();
  } else if (type === 'rent') {
    document.getElementById('yield-rent-text').value = value.toLocaleString();
  }
  calculateYield();
}

function handleYieldTextInput(textInput, type) {
  let valueStr = textInput.value.replace(/\D/g, '');
  let value = parseInt(valueStr, 10) || 0;
  
  if (type === 'price') {
    if (value > 50000000) value = 50000000;
    textInput.value = value.toLocaleString();
    
    // Sync slider
    const slider = document.getElementById('yield-price-range');
    if (value >= slider.min && value <= slider.max) {
      slider.value = value;
    } else if (value < slider.min) {
      slider.value = slider.min;
    } else if (value > slider.max) {
      slider.value = slider.max;
    }
  } else if (type === 'rent') {
    if (value > 1000000) value = 1000000;
    textInput.value = value.toLocaleString();
    
    // Sync slider
    const slider = document.getElementById('yield-rent-range');
    if (value >= slider.min && value <= slider.max) {
      slider.value = value;
    } else if (value < slider.min) {
      slider.value = slider.min;
    } else if (value > slider.max) {
      slider.value = slider.max;
    }
  }
  
  calculateYield();
}

function handleYieldExpensesInput(textInput, type) {
  let valueStr = textInput.value.replace(/\D/g, '');
  let value = parseInt(valueStr, 10) || 0;
  
  if (value > 10000000) value = 10000000; // Cap at 10M for sanity check
  textInput.value = value.toLocaleString();
  
  calculateYield();
}

function calculateYield() {
  const priceEl = document.getElementById('yield-price-text');
  const rentEl = document.getElementById('yield-rent-text');
  if (!priceEl || !rentEl) return;
  
  const priceInput = priceEl.value;
  const rentInput = rentEl.value;
  
  const propertyPrice = parseInt(priceInput.replace(/\D/g, ''), 10) || 0;
  const monthlyRent = parseInt(rentInput.replace(/\D/g, ''), 10) || 0;
  
  const purchaseCostsEl = document.getElementById('yield-purchase-costs-cash');
  const annualExpensesEl = document.getElementById('yield-annual-expenses-cash');
  
  const oneTimePurchaseCosts = purchaseCostsEl ? parseInt(purchaseCostsEl.value.replace(/\D/g, ''), 10) || 0 : 0;
  const annualExpenses = annualExpensesEl ? parseInt(annualExpensesEl.value.replace(/\D/g, ''), 10) || 0 : 0;
  
  // 1. Gross Calculations
  const annualGrossIncome = monthlyRent * 12;
  const grossYield = propertyPrice > 0 ? (annualGrossIncome / propertyPrice) * 100 : 0;
  
  // 2. Net Calculations
  const totalInvestment = propertyPrice + oneTimePurchaseCosts;
  
  const annualNetIncome = Math.max(0, annualGrossIncome - annualExpenses);
  const netYield = totalInvestment > 0 ? (annualNetIncome / totalInvestment) * 100 : 0;
  
  // 3. Render Results
  document.getElementById('yield-gross-value').textContent = `${grossYield.toFixed(2)}%`;
  document.getElementById('yield-net-value').textContent = `${netYield.toFixed(2)}%`;
  
  if (currentLanguage === 'he') {
    document.getElementById('yield-gross-annual-income').textContent = `${annualGrossIncome.toLocaleString()} ₪`;
    document.getElementById('yield-net-annual-income').textContent = `${annualNetIncome.toLocaleString()} ₪`;
    document.getElementById('yield-total-investment').textContent = `${totalInvestment.toLocaleString()} ₪`;
  } else {
    document.getElementById('yield-gross-annual-income').textContent = `₪ ${annualGrossIncome.toLocaleString()}`;
    document.getElementById('yield-net-annual-income').textContent = `₪ ${annualNetIncome.toLocaleString()}`;
    document.getElementById('yield-total-investment').textContent = `₪ ${totalInvestment.toLocaleString()}`;
  }
}

// ==========================================================================
// Articles Slider Carousel Functionality
// ==========================================================================
function slideArticles(direction) {
  const container = document.getElementById('articles-slider-container');
  if (!container) return;
  
  const card = container.querySelector('.article-card');
  if (!card) return;
  
  const cardWidth = card.offsetWidth;
  const gap = 40; // 2.5rem = 40px
  const scrollAmount = cardWidth + gap;
  const isRtl = document.documentElement.dir === 'rtl';
  
  container.scrollBy({
    left: direction * scrollAmount * (isRtl ? -1 : 1),
    behavior: 'smooth'
  });
}

// ==========================================================================
// Update slider navigation arrows visibility based on scroll position
// ==========================================================================
function updateSliderArrows() {
  const container = document.getElementById('articles-slider-container');
  if (!container) return;
  
  const prevBtn = document.querySelector('.slider-arrow-prev');
  const nextBtn = document.querySelector('.slider-arrow-next');
  if (!prevBtn || !nextBtn) return;
  
  const scrollLeft = container.scrollLeft;
  const scrollWidth = container.scrollWidth;
  const clientWidth = container.clientWidth;
  
  const absScrollLeft = Math.abs(scrollLeft);
  const isAtStart = absScrollLeft <= 15;
  const isAtEnd = absScrollLeft + clientWidth >= scrollWidth - 15;
  
  if (isAtStart) {
    prevBtn.style.opacity = '0';
    prevBtn.style.pointerEvents = 'none';
    prevBtn.style.transform = 'translateY(-50%) scale(0.8)';
  } else {
    prevBtn.style.opacity = '1';
    prevBtn.style.pointerEvents = 'auto';
    prevBtn.style.transform = 'translateY(-50%) scale(1)';
  }
  
  if (isAtEnd) {
    nextBtn.style.opacity = '0';
    nextBtn.style.pointerEvents = 'none';
    nextBtn.style.transform = 'translateY(-50%) scale(0.8)';
  } else {
    nextBtn.style.opacity = '1';
    nextBtn.style.pointerEvents = 'auto';
    nextBtn.style.transform = 'translateY(-50%) scale(1)';
  }
}
