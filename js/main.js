/*
   ==========================================================================
   Adv. Eliram Elgarably - Premium Real Estate Law Firm Website
   Interactive Engine & Functionality
   ==========================================================================
*/

// GLOBAL STATE
let currentLanguage = 'he';
let currentPropertyType = 'single'; // 'single', 'additional', or 'immigrant'
let isGiftProperty = false;

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

function initMobileNav() {
  const hamburger = document.getElementById('mobile-nav-toggle');
  const menu = document.getElementById('nav-menu');
  const menuLinks = document.querySelectorAll('#nav-menu .nav-link');

  const toggleMenu = () => {
    hamburger.classList.toggle('active');
    menu.classList.toggle('active');
  };

  hamburger.addEventListener('click', toggleMenu);

  // Close menu drawer when links are clicked
  menuLinks.forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      menu.classList.remove('active');
    });
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
  
  // Update UI state of buttons
  const singleCard = document.getElementById('radio-single-home');
  const additionalCard = document.getElementById('radio-additional-home');
  const immigrantCard = document.getElementById('radio-immigrant-home');
  
  // Reset active classes
  singleCard.classList.remove('active');
  additionalCard.classList.remove('active');
  immigrantCard.classList.remove('active');
  
  if (type === 'single') {
    singleCard.classList.add('active');
    document.getElementById('prop-single').checked = true;
  } else if (type === 'additional') {
    additionalCard.classList.add('active');
    document.getElementById('prop-additional').checked = true;
  } else if (type === 'immigrant') {
    immigrantCard.classList.add('active');
    document.getElementById('prop-immigrant').checked = true;
  }
  
  calculatePurchaseTax();
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
  
  const brackets = TAX_BRACKETS[currentPropertyType];
  const listContainer = document.getElementById('tax-breakdown-list');
  if (!listContainer) return;
  listContainer.innerHTML = '';
  
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
// Contact Form Submission (Mocking & Loader Screens)
// ==========================================================================
function handleFormSubmit(event) {
  event.preventDefault();
  
  const overlay = document.getElementById('form-loading-overlay');
  const spinner = document.getElementById('form-spinner');
  const checkmark = document.getElementById('form-success-checkmark');
  const title = document.getElementById('form-overlay-title');
  const sub = document.getElementById('form-overlay-sub');
  
  const langText = TRANSLATIONS[currentLanguage];
  
  // Show sending screen
  overlay.className = 'form-loading-overlay active';
  spinner.style.display = 'block';
  checkmark.style.display = 'none';
  title.innerHTML = `<span>${langText.sending}</span>`;
  sub.innerHTML = `<span>${langText.pleaseWait}</span>`;
  
  // Simulate network request for 1.8 seconds
  setTimeout(() => {
    // Transition to success screen
    overlay.className = 'form-loading-overlay active success';
    spinner.style.display = 'none';
    checkmark.style.display = 'flex';
    title.innerHTML = `<span>${langText.successTitle}</span>`;
    sub.innerHTML = `<span>${langText.successSub}</span>`;
    
    // Add close button dynamically
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
    
  }, 1800);
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
