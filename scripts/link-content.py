#!/usr/bin/env python3
import os
import re
import json

# 9 Practice Areas Configuration
PRACTICE_AREAS = {
    'second-hand-property': {
        'id': 'second-hand-property',
        'he': 'עסקאות יד שנייה',
        'en': 'Second-Hand Property',
        'keywordsHe': ['יד שנייה', 'יד שניה', 'דירת יד שנייה', 'רכישת דירת יד', 'חוזה מכר', 'רישום הזכויות', 'טאבו'],
        'keywordsEn': ['second-hand', 'pre-owned', 'existing home', 'existing property', 'tabu', 'land registry']
    },
    'new-contractor-purchase': {
        'id': 'new-contractor-purchase',
        'he': 'רכישה מקבלן',
        'en': 'New Contractor Purchase',
        'keywordsHe': ['מקבלן', 'דירה חדשה', 'דירה מקבלן', 'חוק המכר', 'ערבות בנקאית', 'פרויקט חדש', 'קבלן'],
        'keywordsEn': ['contractor', 'developer', 'new construction', 'new apartment', 'bank guarantee']
    },
    'urban-renewal': {
        'id': 'urban-renewal',
        'he': 'התחדשות עירונית',
        'en': 'Urban Renewal',
        'keywordsHe': ['התחדשות עירונית', 'תמ"א 38', 'תמא 38', 'פינוי בינוי', 'תמ״א', 'יזם', 'פינוי-בינוי', 'חיזוק'],
        'keywordsEn': ['urban renewal', 'tma 38', 'pinui binui', 'developer', 'reinforcement', 'regeneration']
    },
    'real-estate-taxation': {
        'id': 'real-estate-taxation',
        'he': 'מיסוי מקרקעין',
        'en': 'Real Estate Taxation',
        'keywordsHe': ['מיסוי מקרקעין', 'מס שבח', 'מס רכישה', 'היטל השבחה', 'פטור ממס', 'תכנון מס', 'שומת מס', 'ועדת ערר'],
        'keywordsEn': ['taxation', 'mas shevach', 'mas rechisha', 'betterment levy', 'tax planning', 'tax exemption']
    },
    'commercial-properties': {
        'id': 'commercial-properties',
        'he': 'נדל״ן מסחרי',
        'en': 'Commercial Properties',
        'keywordsHe': ['נדל"ן מסחרי', 'נדל״ן מסחרי', 'נכס מניב', 'נכס מסחרי', 'משרדים', 'חנויות', 'חוזה שכירות מסחרי'],
        'keywordsEn': ['commercial', 'yield property', 'office space', 'retail space', 'commercial lease']
    },
    'partnerships-coownership': {
        'id': 'partnerships-coownership',
        'he': 'הסכמי שיתוף',
        'en': 'Partnerships & Co-ownership',
        'keywordsHe': ['הסכמי שיתוף', 'פירוק שיתוף', 'מושע', 'שיתוף במקרקעין', 'חלוקת מקרקעין'],
        'keywordsEn': ['co-ownership', 'partnership agreement', 'partition', 'joint ownership', 'mushea']
    },
    'wills-inheritance': {
        'id': 'wills-inheritance',
        'he': 'צוואות וירושות',
        'en': 'Wills & Inheritance',
        'keywordsHe': ['צואה', 'צוואות', 'ירושה', 'ירושות', 'עיזבון', 'צו ירושה', 'צו קיום צוואה'],
        'keywordsEn': ['will', 'wills', 'inheritance', 'succession', 'estate planning', 'probate']
    },
    'ongoing-power-of-attorney': {
        'id': 'ongoing-power-of-attorney',
        'he': 'ייפוי כוח מתמשך',
        'en': 'Ongoing POA',
        'keywordsHe': ['ייפוי כוח מתמשך', 'ייפוי כח מתמשך', 'יפויי כוח מתמשך', 'מיופה כוח', 'אפוטרופסות', 'כשרות משפטית'],
        'keywordsEn': ['ongoing power of attorney', 'poa', 'durable power', 'guardianship', 'attorney-in-fact']
    },
    'corporate-non-profit-registration': {
        'id': 'corporate-non-profit-registration',
        'he': 'רישום חברות ועמותות',
        'en': 'Corporate & Non-Profit',
        'keywordsHe': ['רישום חברות', 'עמותות', 'רישום עמותה', 'רשם החברות', 'רשם העמותות', 'חברה בע"מ', 'תקנון'],
        'keywordsEn': ['corporate registration', 'non-profit', 'incorporation', 'association', 'bylaws']
    }
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, 'articles')
EN_ARTICLES_DIR = os.path.join(BASE_DIR, 'en', 'articles')
PRACTICE_DIR = os.path.join(BASE_DIR, 'practice')
EN_PRACTICE_DIR = os.path.join(BASE_DIR, 'en', 'practice')

def main():
    print('--- Starting Content Automation Linker (Python version) ---')
    
    # 1. Scan and Classify Articles
    articles = scan_articles()
    print(f'Found {len(articles)} articles to process.')
    
    # Save classification database
    db_path = os.path.join(BASE_DIR, 'assets', 'articles_db.json')
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)
    print('Saved classification database to: assets/articles_db.json')
    
    # 2. Rewrite Homepage Article Badges
    update_homepages(articles)
    
    # 3. Rewrite Articles Index Card Badges
    update_articles_indexes(articles)
    
    # 4. Inject Back Links in Article Detail pages
    update_article_details(articles)
    
    # 5. Inject Related Articles in Practice subpages
    update_practice_pages(articles)
    
    print('--- Content Automation Linker Completed Successfully ---')

def scan_articles():
    folders = [f for f in os.listdir(ARTICLES_DIR) if os.path.isdir(os.path.join(ARTICLES_DIR, f))]
    articles_list = []
    
    for slug in folders:
        he_file_path = os.path.join(ARTICLES_DIR, slug, 'index.html')
        en_file_path = os.path.join(EN_ARTICLES_DIR, slug, 'index.html')
        
        if not os.path.exists(he_file_path) or not os.path.exists(en_file_path):
            print(f'Warning: Missing files for slug: {slug}')
            continue
            
        with open(he_file_path, 'r', encoding='utf-8') as f:
            html_he = f.read()
        with open(en_file_path, 'r', encoding='utf-8') as f:
            html_en = f.read()
            
        title_he = extract_tag_content(html_he, 'h1', 'article-detail-title', 'he')
        title_en = extract_tag_content(html_he, 'h1', 'article-detail-title', 'en')
        desc_he = extract_meta_description(html_he)
        desc_en = extract_meta_description(html_en)
        date = extract_date(html_he)
        read_time = extract_read_time(html_he)
        image = extract_image_name(html_he)
        
        body_he = extract_body_text(html_he)
        body_en = extract_body_text(html_en)
        
        classification = classify(title_he, title_en, desc_he, desc_en, body_he, body_en)
        
        articles_list.append({
            'slug': slug,
            'titleHe': title_he,
            'titleEn': title_en,
            'descHe': desc_he,
            'descEn': desc_en,
            'date': date,
            'readTime': read_time,
            'image': image,
            'practiceAreaId': classification['practiceAreaId'],
            'classificationConfidence': classification['confidence'],
            'needsReview': classification['needsReview'],
            'tags': classification['tags']
        })
        
        print(f"Classified: [{slug}] -> {classification['practiceAreaId']} (Conf: {classification['confidence']:.2f}, NeedsReview: {classification['needsReview']})")
        
    return articles_list

def extract_tag_content(html, tag, class_name, lang):
    regex = re.compile(rf'<{tag}[^>]*class="[^"]*{class_name}[^"]*"[^>]*>([\s\S]*?)</{tag}>')
    match = regex.search(html)
    if not match:
        return ''
    
    inner_html = match.group(1)
    lang_regex = re.compile(rf'<span[^>]*lang="{lang}"[^>]*>([\s\S]*?)</span>')
    lang_match = lang_regex.search(inner_html)
    return lang_match.group(1).strip() if lang_match else ''

def extract_meta_description(html):
    match = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', html, re.IGNORECASE)
    return match.group(1).strip() if match else ''

def extract_date(html):
    match = re.search(r'<div[^>]*class="[^"]*article-(?:detail-)?meta[^"]*"[^>]*>[\s\S]*?<span>(\d{2}\.\d{2}\.\d{4})<\/span>', html)
    return match.group(1) if match else '01.06.2026'

def extract_read_time(html):
    match = re.search(r'<div[^>]*class="[^"]*article-(?:detail-)?meta[^"]*"[^>]*>[\s\S]*?<span>(\d+\s*min\s*read)<\/span>', html, re.IGNORECASE)
    return match.group(1) if match else '4 min read'

def extract_image_name(html):
    # Target the article hero image inside .article-detail-hero wrapper specifically
    match = re.search(r'<div[^>]*class="[^"]*article-detail-hero[^"]*"[^>]*>[\s\S]*?<img[^>]*src="[^"]*assets\/([^"]+)"', html)
    if match:
        return match.group(1)
    # Fallback to general assets image
    match = re.search(r'<img[^>]*src="[^"]*assets\/([^"]+)"', html)
    return match.group(1) if match else 'article_second_hand.png'

def extract_body_text(html):
    match = re.search(r'<div[^>]*class="[^"]*article-body-text[^"]*"[^>]*>([\s\S]*?)<\/div>', html)
    if not match:
        return ''
    # Strip HTML tags
    return re.sub(r'<[^>]+>', ' ', match.group(1))

def classify(title_he, title_en, desc_he, desc_en, body_he, body_en):
    best_area = 'second-hand-property'
    max_score = 0
    total_score = 0
    best_tags = []
    
    combined_he = f"{title_he} {desc_he} {body_he}".lower()
    combined_en = f"{title_en} {desc_en} {body_en}".lower()
    
    for id_key, area in PRACTICE_AREAS.items():
        score = 0
        matched_tags = []
        
        # Hebrew keyword scoring
        for kw in area['keywordsHe']:
            escaped_kw = re.escape(kw)
            matches_title = len(re.findall(escaped_kw, title_he, re.IGNORECASE))
            matches_desc = len(re.findall(escaped_kw, desc_he, re.IGNORECASE))
            matches_body = len(re.findall(escaped_kw, body_he, re.IGNORECASE))
            
            score += matches_title * 10
            score += matches_desc * 5
            score += matches_body * 1
            
            if matches_title > 0 or matches_desc > 0 or matches_body > 0:
                matched_tags.append(kw)
                
        # English keyword scoring
        for kw in area['keywordsEn']:
            escaped_kw = re.escape(kw)
            matches_title = len(re.findall(escaped_kw, title_en, re.IGNORECASE))
            matches_desc = len(re.findall(escaped_kw, desc_en, re.IGNORECASE))
            matches_body = len(re.findall(escaped_kw, body_en, re.IGNORECASE))
            
            score += matches_title * 10
            score += matches_desc * 5
            score += matches_body * 1
            
            if matches_title > 0 or matches_desc > 0 or matches_body > 0:
                matched_tags.append(kw)
                
        total_score += score
        if score > max_score:
            max_score = score
            best_area = id_key
            best_tags = matched_tags
            
    confidence = max_score / total_score if total_score > 0 else 0
    needs_review = confidence < 0.6 or max_score < 5
    
    return {
        'practiceAreaId': best_area,
        'confidence': confidence,
        'needs_review': needs_review,
        'needsReview': needs_review,
        'tags': best_tags[:4]
    }

def render_article_card(article, lang, rel_site, rel_lang):
    article_url = f"{rel_lang}articles/{article['slug']}/index.html"
    image_url = f"{rel_site}assets/{article['image']}"
    author_img_url = f"{rel_site}assets/eliram_profile.jpg"
    practice_url = f"{rel_lang}practice/{article['practiceAreaId']}/index.html"
    practice_area = PRACTICE_AREAS[article['practiceAreaId']]
    
    title_title = article['titleHe'] if lang == 'he' else article['titleEn']

    return f"""            <article class="article-card">
              <div class="article-card-image-wrapper">
                <img src="{image_url}" alt="{title_title}" class="article-card-image">
                <a href="{practice_url}" class="article-badge">
                  <span lang="he">{practice_area['he']}</span>
                  <span lang="en">{practice_area['en']}</span>
                </a>
              </div>
              <div class="article-card-content">
                <div class="article-card-meta">
                  <span>{article['date']}</span>
                  <span class="meta-dot">•</span>
                  <span>{article['readTime']}</span>
                </div>
                <h3 class="article-card-title">
                  <a href="{article_url}">
                    <span lang="he">{article['titleHe']}</span>
                    <span lang="en">{article['titleEn']}</span>
                  </a>
                </h3>
                <p class="article-card-desc">
                  <span lang="he">{article['descHe']}</span>
                  <span lang="en">{article['descEn']}</span>
                </p>
                <div class="article-author">
                  <div class="author-avatar-wrapper">
                    <img src="{author_img_url}" alt="{"עו״ד אלירם אלגרבלי" if lang == 'he' else "Adv. Eliram Elgarably"}" class="author-avatar">
                  </div>
                  <div class="author-info">
                    <span class="author-name">
                      <span lang="he">עו״ד אלירם אלגרבלי</span>
                      <span lang="en">Adv. Eliram Elgarably</span>
                    </span>
                    <span class="author-title">
                      <span lang="he">מומחה למקרקעין</span>
                      <span lang="en">Real Estate Attorney</span>
                    </span>
                  </div>
                </div>
              </div>
            </article>"""

def update_homepages(articles):
    paths = [
        {'file': os.path.join(BASE_DIR, 'index.html'), 'lang': 'he', 'relSite': '', 'relLang': ''},
        {'file': os.path.join(BASE_DIR, 'en', 'index.html'), 'lang': 'en', 'relSite': '../', 'relLang': ''}
    ]
    
    for p in paths:
        if not os.path.exists(p['file']):
            continue
        with open(p['file'], 'r', encoding='utf-8') as f:
            html = f.read()
            
        track_regex = re.compile(r'<!-- ARTICLES_TRACK_START -->[\s\S]*?<!-- ARTICLES_TRACK_END -->')
        
        # Sort articles consistently to maintain chronological order
        sorted_articles = sorted(articles, key=lambda x: x['slug'], reverse=True)
        new_cards_html = '\n\n'.join([render_article_card(a, p['lang'], p['relSite'], p['relLang']) for a in sorted_articles])
        
        new_track = f'<!-- ARTICLES_TRACK_START -->\n          <div class="articles-slider-track">\n{new_cards_html}\n          </div>\n          <!-- ARTICLES_TRACK_END -->'
        html = track_regex.sub(new_track, html)
        
        with open(p['file'], 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated homepage: {p['file']}")

def update_articles_indexes(articles):
    paths = [
        {'file': os.path.join(BASE_DIR, 'articles', 'index.html'), 'lang': 'he', 'relSite': '../', 'relLang': '../'},
        {'file': os.path.join(BASE_DIR, 'en', 'articles', 'index.html'), 'lang': 'en', 'relSite': '../../', 'relLang': '../'}
    ]
    
    for p in paths:
        if not os.path.exists(p['file']):
            continue
        with open(p['file'], 'r', encoding='utf-8') as f:
            html = f.read()
            
        grid_regex = re.compile(r'<!-- ARTICLES_GRID_START -->[\s\S]*?<!-- ARTICLES_GRID_END -->')
        
        sorted_articles = sorted(articles, key=lambda x: x['slug'], reverse=True)
        new_cards_html = '\n\n'.join([render_article_card(a, p['lang'], p['relSite'], p['relLang']) for a in sorted_articles])
        
        new_grid = f'<!-- ARTICLES_GRID_START -->\n      <div class="articles-grid">\n{new_cards_html}\n      </div>\n      <!-- ARTICLES_GRID_END -->'
        html = grid_regex.sub(new_grid, html)
        
        with open(p['file'], 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated articles index: {p['file']}")

def update_article_details(articles):
    for article in articles:
        paths = [
            {'file': os.path.join(ARTICLES_DIR, article['slug'], 'index.html'), 'lang': 'he', 'rootRel': '../../'},
            {'file': os.path.join(EN_ARTICLES_DIR, article['slug'], 'index.html'), 'lang': 'en', 'rootRel': '../../'}
        ]
        
        practice_area = PRACTICE_AREAS[article['practiceAreaId']]
        
        for p in paths:
            if not os.path.exists(p['file']):
                continue
            with open(p['file'], 'r', encoding='utf-8') as f:
                html = f.read()
                
            footer_regex = re.compile(r'<div class="article-detail-footer">([\s\S]*?)</div>')
            
            back_to_articles = '../index.html'
            back_to_practice = f"{p['rootRel']}practice/{article['practiceAreaId']}/index.html"
            contact_url = f"{p['rootRel']}index.html#contact"
            
            new_footer_content = f"""<div class="article-detail-footer">
            <a href="{back_to_articles}" class="btn btn-outline btn-sm">
              <span lang="he">← חזרה למאמרים</span>
              <span lang="en">← Back to Articles</span>
            </a>
            <!-- BACK_TO_PRACTICE_START -->
            <a href="{back_to_practice}" class="btn btn-outline btn-sm">
              <span lang="he">← לתחום התמחות: {practice_area['he']}</span>
              <span lang="en">← Practice Area: {practice_area['en']}</span>
            </a>
            <!-- BACK_TO_PRACTICE_END -->
            <a href="{contact_url}" class="btn btn-gold btn-sm">
              <span lang="he">להתייעצות אישית</span>
              <span lang="en">Get Advice</span>
            </a>
          </div>"""
          
            html = footer_regex.sub(new_footer_content, html)
            
            # Convert article badge to link pointing to the practice area
            badge_regex = re.compile(r'<(div|a) class="article-badge" style="position: static;"[^>]*>([\s\S]*?)</\1>', re.IGNORECASE)
            badge_link = f"../../practice/{article['practiceAreaId']}/index.html"
            new_badge = f'<a href="{badge_link}" class="article-badge" style="position: static; text-decoration: none;">\\2</a>'
            html = badge_regex.sub(new_badge, html)
            
            with open(p['file'], 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Updated article detail back-link and badge: {p['file']}")

def update_practice_pages(articles):
    for practice_id, practice_area in PRACTICE_AREAS.items():
        related = [a for a in articles if a['practiceAreaId'] == practice_id]
        
        paths = [
            {'file': os.path.join(PRACTICE_DIR, practice_id, 'index.html'), 'lang': 'he', 'relSite': '../../', 'relLang': '../../'},
            {'file': os.path.join(EN_PRACTICE_DIR, practice_id, 'index.html'), 'lang': 'en', 'relSite': '../../../', 'relLang': '../../'}
        ]
        
        for p in paths:
            if not os.path.exists(p['file']):
                continue
            with open(p['file'], 'r', encoding='utf-8') as f:
                html = f.read()
                
            # Render related articles grid
            related_html = ''
            if len(related) > 0:
                cards_html = '\n\n'.join([render_article_card(a, p['lang'], p['relSite'], p['relLang']) for a in related])
                related_html = f"""<!-- RELATED_ARTICLES_START -->
        <div class="related-articles-section">
          <h3 class="related-articles-title">
            <span lang="he">מאמרים ומדריכים קשורים</span>
            <span lang="en">Related Articles & Guides</span>
          </h3>
          <div class="related-articles-grid">
{cards_html}
          </div>
        </div>
        <!-- RELATED_ARTICLES_END -->"""
            else:
                related_html = "<!-- RELATED_ARTICLES_START -->\n        <!-- RELATED_ARTICLES_END -->"
                
            marker_regex = re.compile(r'<!-- RELATED_ARTICLES_START -->[\s\S]*?<!-- RELATED_ARTICLES_END -->')
            if marker_regex.search(html):
                html = marker_regex.sub(related_html, html)
            else:
                cta_end_regex = re.compile(r'</div>\s*</div>\s*</div>\s*</main>')
                if cta_end_regex.search(html):
                    replacement = f"\n        {related_html}\n      </div>\n    </div>\n  </main>"
                    html = cta_end_regex.sub(replacement, html)
                    
            with open(p['file'], 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Updated practice page related articles: {p['file']} ({len(related)} articles linked)")

if __name__ == '__main__':
    main()
