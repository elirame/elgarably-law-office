# Adv. Eliram Elgarably - Premium Real Estate Law Firm Website

A premium, luxury, responsive, and fully interactive single-page law firm website developed for **Adv. Eliram Elgarably** (established in real estate law since 2013).

This website features modern HTML5, CSS3, and ES6+ JS built from scratch. It showcases premium aesthetics (deep navy, charcoal, and luxury gold), dynamic bilingual switching (Hebrew & English), scroll reveal animations, and an interactive Purchase Tax Calculator.

---

## Key Features

1. **Bilingual Toggle System**: Easily switch between עברית (Hebrew) and English. Layout shifts from RTL to LTR dynamically using modern CSS Logical Properties (without requiring separate stylesheets).
2. **Interactive Purchase Tax Simulator**: An interactive tool based on standard Israeli residential purchase tax brackets (2026 update). Computes taxes in real-time for Single Properties vs. Investment/Additional Properties, providing a clear bracket-by-bracket breakdown in the selected language.
3. **Premium Visual System**: Stunning high-resolution visual assets including a luxury logo, hero banner depicting modern Tel Aviv architecture at sunset, and professional portrait.
4. **Scroll reveal counters**: Numbers count up from zero once stats (years of practice, transactions, saved tax) scroll into view.
5. **Dynamic FAQ Accordions**: Smooth opening and closing FAQs with arrow indicators.
6. **Luxury Consultation Contact Form**: Dynamic floating label inputs, validation indicator styling (`:user-valid` / `:user-invalid`), and submission spinner with a final success screen.

---

## Directory Structure

* `index.html`: Web layout structure and bilingual text tags.
* `styles/main.css`: Core stylesheet containing the responsive variables, CSS logical properties, glassmorphism overlays, animations, and typography rules.
* `js/main.js`: Interactive events, RTL/LTR layout toggles, stats counters, accordion mechanics, purchase tax calculator math, and form feedback systems.
* `assets/`:
  * `logo.png`: Golden scales and house integration logo.
  * `hero.png`: Tel Aviv sunset skyscraper hero wallpaper.
  * `portrait.png`: Professional portrait of Israeli attorney in office.
* `disclaimer.html`: Bilingual disclaimer and legal warnings.
* `privacy.html`: Bilingual privacy policy document.

---

## Local Setup & Development

No heavy compilation or Node packages are required. To view and test the website locally:

1. Open your terminal.
2. Navigate to this project directory:
   ```bash
   cd /Users/eliram/.gemini/antigravity/scratch/elgarably-law-office
   ```
3. Start Python's built-in HTTP server:
   ```bash
   python3 -m http.server 8000
   ```
4. Open your web browser and go to:
   [http://localhost:8000](http://localhost:8000)

---

## How to Customize Your Portrait Image

To replace the placeholder portrait with your own professional photo:
1. Crop your professional photograph to a square aspect ratio (e.g., `800x800px` or `1000x1000px`).
2. Export it as a PNG file named `portrait.png`.
3. Overwrite the file at `/Users/eliram/.gemini/antigravity/scratch/elgarably-law-office/assets/portrait.png`.
4. Refresh the webpage. The site will instantly display your personal picture wrapped in the luxury double gold frames!
