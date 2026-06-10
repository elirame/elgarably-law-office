import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, 'articles')
EN_ARTICLES_DIR = os.path.join(BASE_DIR, 'en', 'articles')

# 27 Articles Data
ARTICLES_DATA = [
    # --- Category 1: Second-Hand Property ---
    {
        'slug': 'due-diligence-second-hand-home',
        'practiceAreaId': 'second-hand-property',
        'image': 'article_second_hand_1.png',
        'date': '09.06.2026',
        'readTime': '5 min read',
        'categoryHe': 'עסקאות יד שנייה',
        'categoryEn': 'Second-Hand Property',
        'titleHe': 'המדריך המלא לבדיקות מקדמיות לפני רכישת דירה יד שנייה',
        'titleEn': 'The Complete Due Diligence Guide Before Buying a Second-Hand Property',
        'descHe': 'מה בודקים בנסח טאבו, ברשות מקרקעי ישראל ובתיק הבניין בעירייה, ולמה בדיקה אחת חסרה עלולה לעלות מאות אלפי שקלים.',
        'descEn': 'What to check in the Land Registry (Tabu), Israel Land Authority, and municipal files, and why missing one check can cost you hundreds of thousands.',
        'contentHe': """
            <p>רכישת דירה יד שנייה היא אחת העסקאות הפיננסיות המשמעותיות ביותר בחייו של אדם. על מנת להבטיח כי כספכם מושקע בבטחה וכי לא תתקלו בהפתעות לא נעימות לאחר החתימה, יש לבצע סדרת בדיקות מקדמיות יסודיות ומקיפות.</p>
            
            <h2>1. הבדיקה הקניינית: נסח טאבו ורישום זכויות</h2>
            <p>השלב הראשון והקריטי ביותר הוא בדיקת נסח הטאבו העדכני של הנכס. נסח הטאבו מספק תעודת זהות משפטית מלאה לדירה. יש לוודא כי המוכר רשום כבעלים הבלעדי של הנכס, וכי אין על הנכס שעבודים, עיקולים, הערות אזהרה לטובת צדדים שלישיים או משכנתאות קודמות שטרם נמחקו. במקרה שהנכס רשום ברשות מקרקעי ישראל או בחברה משכנת, יש להנפיק אישור זכויות עדכני המעיד על מצב הזכויות הנוכחי.</p>
            
            <h2>2. הבדיקה התכנונית: תיק הבניין בעירייה והיתר בנייה</h2>
            <p>רוכשים רבים נוטים לוותר על בדיקה זו, אך היא חיונית ביותר. יש לגשת למחלקת ההנדסה בעירייה הרלוונטית ולהזמין את תיק הבניין של הנכס. מטרת הבדיקה היא להשוות בין היתר הבנייה המקורי ותשריט הבית המשותף לבין המצב הקיים בפועל בשטח. בדיקה זו מאפשרת לגלות חריגות בנייה, סגירת מרפסות ללא היתר, פיצול דירות לא חוקי או צווי הריסה תלויים ועומדים, שעלולים למנוע קבלת משכנתא ולהוביל להליכים משפטיים יקרים.</p>
            
            <h2>3. הבדיקה הפיזית ומצב התשתיות</h2>
            <p>מעבר לבדיקות המשפטיות, מומלץ לבצע בדיקה פיזית של הנכס באמצעות מהנדס או חברת בדק בית מקצועית. הבדיקה תחשוף ליקויי רטיבות סמויים, בעיות אינסטלציה, סדקים קונסטרוקטיביים ותקלות במערכת החשמל. גילוי ליקויים אלו מראש יאפשר לכם לנהל משא ומתן יעיל על מחיר הנכס או לדרוש מהמוכר לתקנם טרם העברת החזקה.</p>
        """,
        'contentEn': """
            <p>Purchasing a second-hand apartment is one of the most significant financial transactions in a person's life. To ensure that your money is invested safely and that you will not encounter unpleasant surprises after signing, it is essential to conduct a thorough and comprehensive series of preliminary checks.</p>
            
            <h2>1. Proprietary Inspection: Land Registry and Title Verification</h2>
            <p>The first and most critical step is inspecting the up-to-date Tabu (Land Registry) extract of the property. The Tabu extract provides a full legal identity card for the apartment. You must verify that the seller is registered as the sole owner of the property, and that there are no pledges, attachments, warning notes in favor of third parties, or active mortgages that have not yet been discharged.</p>
            
            <h2>2. Planning Inspection: The Municipal Building File and Permits</h2>
            <p>Many buyers tend to skip this check, but it is vital. You should visit the engineering department of the relevant municipality and order the building file. The purpose of this inspection is to compare the original building permit and the condominium map (Tashrit) with the actual physical state of the property. This reveals building violations, unpermitted balcony enclosures, illegal apartment splitting, or outstanding demolition orders.</p>
            
            <h2>3. Physical Due Diligence and Infrastructure</h2>
            <p>Beyond legal checks, it is highly recommended to perform a physical inspection of the property using a qualified engineer or a professional home inspection company. This will uncover hidden moisture issues, plumbing defects, structural cracks, and electrical faults, allowing you to renegotiate the price or demand repairs prior to closing.</p>
        """
    },
    {
        'slug': 'warning-note-importance',
        'practiceAreaId': 'second-hand-property',
        'image': 'article_second_hand_2.png',
        'date': '08.06.2026',
        'readTime': '4 min read',
        'categoryHe': 'עסקאות יד שנייה',
        'categoryEn': 'Second-Hand Property',
        'titleHe': 'הערת אזהרה: השריון המשפטי החשוב ביותר של רוכש דירה',
        'titleEn': 'Warning Note: The Most Crucial Legal Shield for Property Buyers',
        'descHe': 'מהי הערת אזהרה, מתי רושמים אותה, ומה הסיכונים כשמשלמים כסף לפני שהיא נרשמה.',
        'descEn': 'What is a warning note (He`arat Azhara), when is it registered, and the risks of paying money before it is secured.',
        'contentHe': """
            <p>בעת חתימה על חוזה לרכישת נדל"ן, נוצר פער זמנים מובנה בין מועד החתימה ותשלום הכספים הראשונים לבין רישום הבעלות הסופי בטאבו. כדי לגשר על פער זה ולהגן על כספי הרוכש, המציא החוק הישראלי כלי משפטי רב עוצמה: הערת אזהרה.</p>
            
            <h2>מהי הערת אזהרה?</h2>
            <p>הערת אזהרה היא רישום רשמי בפנקסי המקרקעין (הטאבו) המעיד על התחייבות בכתב של בעל המקרקעין לעשות בהם עסקה, או להימנע מלעשות בהם עסקה. מרגע רישום ההערה לטובת הרוכש, לא ניתן לרשום עסקה סותרת על הנכס ללא הסכמתו של הרוכש או ללא צו בית משפט. בכך, מונעת הערת האזהרה מצב שבו מוכר נוכל מנסה למכור את אותה הדירה למספר קונים שונים במקביל.</p>
            
            <h2>מתי יש לרשום את הערת האזהרה?</h2>
            <p>הכלל המשפטי הנוקשה ביותר בעסקאות מקרקעין הוא: **רישום הערת אזהרה מייד לאחר החתימה**. כפרקטיקה מקובלת, עורך הדין של הרוכש מגיש את הבקשה לרישום הערת האזהרה בטאבו תוך 24 שעות מחתימת ההסכם. יתרה מכך, נהוג להפקיד את התשלום הראשון בנאמנות אצל עורך הדין של המוכר, ולא להעבירו ישירות למוכר עד אשר מתקבל אישור רשמי מהטאבו על רישום מוצלח של הערת האזהרה לטובת הקונה.</p>
            
            <h2>הגנה מפני פשיטת רגל ועיקולים של המוכר</h2>
            <p>מעבר למניעת עסקאות סותרות, הערת האזהרה מעניקה לרוכש עדיפות משפטית מוחלטת על פני נושים אחרים של המוכר. אם לאחר רישום הערת האזהרה יוטל עיקול על נכסי המוכר, או אם המוכר ייכנס להליכי פשיטת רגל או פירוק, זכויותיו של הרוכש מוגנות ולא ניתן יהיה לפגוע בהן או למכור את הנכס לצורך כיסוי חובות המוכר.</p>
        """,
        'contentEn': """
            <p>When signing a real estate purchase agreement, a time gap naturally exists between the date of signing and initial payments and the final registration of ownership. To bridge this gap and protect the buyer\'s funds, Israeli law features a powerful legal tool: the Warning Note (He\'arat Azhara).</p>
            
            <h2>What is a Warning Note?</h2>
            <p>A warning note is an official entry in the Land Registry (Tabu) proving a written commitment by the property owner to execute a transaction, or to refrain from executing one. Once registered in favor of the buyer, no conflicting transaction can be recorded on the property without the buyer\'s consent or a court order, preventing fraudulent double-selling.</p>
            
            <h2>When Should the Warning Note Be Registered?</h2>
            <p>The golden legal rule is: **register the warning note immediately after signing**. Standard practice dictates that the buyer\'s attorney files the registration request within 24 hours of signing. Furthermore, the first payment is typically kept in escrow and not transferred to the seller until the registry officially confirms the warning note registration.</p>
            
            <h2>Protection Against Seller Insolvency and Liens</h2>
            <p>Beyond preventing conflicting sales, a warning note gives the buyer absolute legal priority over the seller\'s other creditors. If liens are placed on the seller\'s assets, or if the seller enters bankruptcy after the warning note is registered, the buyer\'s contractual rights remain fully protected.</p>
        """
    },
    {
        'slug': 'construction-violations-second-hand',
        'practiceAreaId': 'second-hand-property',
        'image': 'article_second_hand_3.png',
        'date': '07.06.2026',
        'readTime': '5 min read',
        'categoryHe': 'עסקאות יד שנייה',
        'categoryEn': 'Second-Hand Property',
        'titleHe': 'חריגות בנייה בדירה יד שנייה — איך מזהים, ומי נושא באחריות?',
        'titleEn': 'Building Violations in Second-Hand Homes: Identification & Liability',
        'descHe': 'ההבדל בין חריגה שניתנת להכשרה לבין כזו שמסכלת עסקה, והשפעתה על המשכנתא ועל מחיר הדירה.',
        'descEn': 'The difference between violations that can be legalized and those that ruin a deal, and their impact on mortgages and pricing.',
        'contentHe': """
            <p>בעת רכישת דירת יד שנייה בישראל, אחד המוקשים המשפטיים והתכנוניים הנפוצים ביותר הוא קיומן של חריגות בנייה. חריגות אלו עלולות להעמיד את הרוכש בסכנה של קבלת צווים שיפוטיים, קנסות כבדים וקשיים משמעותיים בקבלת משכנתא מהבנקים.</p>
            
            <h2>מה נחשב לחריגת בנייה בדירה?</h2>
            <p>חריגת בנייה היא כל שינוי פיזי שבוצע בנכס ללא היתר בנייה כחוק או בניגוד להיתר הקיים. דוגמאות נפוצות כוללות: סגירת מרפסות באמצעות חלונות אלומיניום או בנייה קלה, בניית גלריית עץ בתוך חלל הדירה, הוספת מחסן או סככה בחצר ללא היתר, פיצול הדירה לשתי יחידות דיור נפרדות, או פתיחת חלונות בקירות חיצוניים בניגוד לתוכנית המבנה.</p>
            
            <h2>השפעת החריגה על אישור המשכנתא מהבנק</h2>
            <p>לפני אישור סופי של משכנתא, הבנק שולח שמאי מקרקעין מטעמו לבחון את הדירה. השמאי משווה את המצב הפיזי להיתר הבנייה ומציין במפורש בדוח השמאות קיומן של חריגות בנייה. אם מדובר בחריגות חמורות (כמו פיצול לא חוקי או בנייה בשטחים משותפים), הבנק עלול לסרב להעניק משכנתא לחלוטין, או להפחית באופן משמעותי את שווי הנכס לצורך מתן ההלוואה, מה שיעמיד את הקונה בפני שוקת שבורה.</p>
            
            <h2>מי נושא באחריות וכיצד להתגונן בחוזה?</h2>
            <p>על פי החוק, האחריות הפלילית לקיומן של חריגות בנייה עוברת לבעלים החדש של הדירה עם העברת הבעלות. לכן, חובה לגלות חריגות אלו מראש במסגרת הבדיקות המקדמיות. במידה ומתגלות חריגות שניתן להכשירן, יש לעגן בחוזה המכר מנגנונים ברורים: חיוב המוכר להסדיר את ההיתר על חשבונו לפני מסירת החזקה, או השארת סכומי כסף משמעותיים בנאמנות לצורך הבטחת ההסדרה או הריסה של החריגה במידת הצורך.</p>
        """,
        'contentEn': """
            <p>When purchasing a second-hand apartment in Israel, one of the most common legal and planning pitfalls is the existence of building violations. These violations expose the buyer to judicial orders, heavy fines, and severe difficulties in securing a mortgage.</p>
            
            <h2>What is Considered a Building Violation?</h2>
            <p>A building violation is any physical change made to a property without a lawful permit or in violation of an existing permit. Examples include closing balconies, constructing wooden galleries, adding unpermitted yards sheds, splitting the apartment, or modifying exterior walls.</p>
            
            <h2>Impact of Violations on Mortgage Approval</h2>
            <p>Before issuing a mortgage, banks send an appraiser to evaluate the property. The appraiser compares the physical structure with building permits and explicitly notes any violations. Serious violations can lead to the bank refusing the mortgage or devaluing the property significantly.</p>
            
            <h2>Who is Liable, and How to Protect Yourself?</h2>
            <p>Legally, criminal liability for zoning violations transfers to the new owner upon ownership transfer. Therefore, discovering them during due diligence is essential. If legalizable violations exist, the contract must hold the seller accountable to resolve them or keep substantial funds in escrow to secure compliance.</p>
        """
    },
    # --- Category 2: New Contractor Purchase ---
    {
        'slug': 'sale-law-guarantee-contractor',
        'practiceAreaId': 'new-contractor-purchase',
        'image': 'article_contractor_1.png',
        'date': '06.06.2026',
        'readTime': '5 min read',
        'categoryHe': 'רכישה מקבלן',
        'categoryEn': 'New Contractor Purchase',
        'titleHe': 'ערבות חוק המכר: כך מוודאים שהכסף שלכם מוגן עד קבלת המפתח',
        'titleEn': 'Sale Law Guarantees: Ensuring Your Payments Are Protected from the Developer',
        'descHe': 'סוגי הבטוחות לפי חוק המכר (דירות), ההבדלים ביניהן, ומה לבדוק לפני כל תשלום.',
        'descEn': 'Types of statutory guarantees under the Sale Law, the differences between them, and what to verify before making any payment.',
        'contentHe': """
            <p>קניית דירה "על הנייר" מקבלן מלווה ברמת סיכון משמעותית. הקונה משלם סכומי כסף עצומים לאורך תקופת הבנייה, עוד לפני שהנכס קיים בפועל. כדי להגן על כספי הרוכשים מפני מצבים של קריסת קבלן או פשיטת רגל, חוקק בישראל חוק המכר (דירות) (הבטחת השקעות של רוכשי דירות).</p>
            
            <h2>מהן הבטוחות הנדרשות על פי חוק המכר?</h2>
            <p>החוק קובע כי קבלן אינו רשאי לקבל מרוכש דירה סכום העולה על 7% ממחיר הדירה, אלא אם כן הבטיח את כספי הקונה באחת מחמש דרכים הקבועות בחוק. שתי הבטוחות הנפוצות והחזקות ביותר הן: **ערבות בנקאית** (Bank Guarantee) המונפקת על ידי הבנק המלווה של הפרויקט, או **פוליסת ביטוח** מחברת ביטוח מוכרת. בטוחות אלו מבטיחות כי במקרה שהקבלן לא יוכל למסור את הדירה בשל עיקול, פירוק או פשיטת רגל, יקבל הרוכש את כספו בחזרה במלואו.</p>
            
            <h2>שיטת שובר התשלום (פנקס שוברים)</h2>
            <p>בפרויקטים המלווים על ידי בנק (ליווי פיננסי סגור), הרוכש אינו מעביר כסף ישירות לחשבון הקבלן. במקום זאת, התשלומים מבוצעים אך ורק באמצעות פנקס שוברים ייעודי ישירות לחשבון הליווי של הפרויקט בבנק המלווה. כל הפקדה של שובר תשלום מפעילה אוטומטית הנפקה של ערבות חוק מכר התואמת את הסכום שהופקד. חל איסור מוחלט לשלם לקבלן במזומן, בהעברות בנקאיות לחשבונות אחרים או בצ\'קים שלא דרך השוברים.</p>
            
            <h2>מה יש לבדוק לפני החתימה על ההסכם?</h2>
            <p>במסגרת המשא ומתן על חוזה הרכישה, עורך הדין מטעמכם יוודא כי בהסכם מוגדרים תנאים ברורים להנפקת הערבויות, לוחות זמנים מדויקים למסירתן לידיכם, וכי הבנק המלווה מנפיק מכתב החרגה (מכתב המעניק לערבות תוקף ומחריג את הדירה מהשעבוד של הבנק על הקרקע).</p>
        """,
        'contentEn': """
            <p>Buying an off-plan apartment from a developer carries significant risks. The buyer makes payments throughout construction before the property exists. To protect buyers from developer insolvency, Israeli law mandates the Sale Law (Apartments) (Assuring Investments of Apartment Buyers).</p>
            
            <h2>What Guarantees Are Mandated by the Sale Law?</h2>
            <p>The law states a developer cannot accept payments exceeding 7% of the purchase price unless they secure the funds using one of five methods. The two most common are a **Bank Guarantee** issued by the project\'s lending bank, or an **Insurance Policy**. These ensure buyers get all paid capital back if the builder collapses.</p>
            
            <h2>The Escrow Voucher System (Pinkas Shovarim)</h2>
            <p>In project finance setups, buyers never pay developers directly. Payments must be deposited strictly using designated vouchers into the project\'s secure escrow account. Depositing a voucher triggers the automated issuance of a Sale Law guarantee. Paying in cash or via unauthorized checks is strictly forbidden.</p>
            
            <h2>What to Check Before Contract Signing?</h2>
            <p>During negotiations, your attorney will verify that the agreement defines clear terms for issuing guarantees, precise delivery timelines, and ensure the bank issues a waiver letter (Michtav Hachraga) exempting your apartment from the bank\'s general land mortgage.</p>
        """
    },
    {
        'slug': 'construction-index-linkage',
        'practiceAreaId': 'new-contractor-purchase',
        'image': 'article_contractor_2.png',
        'date': '05.06.2026',
        'readTime': '4 min read',
        'categoryHe': 'רכישה מקבלן',
        'categoryEn': 'New Contractor Purchase',
        'titleHe': 'הצמדה למדד תשומות הבנייה — המלכודת שמייקרת את הדירה בעשרות אלפי שקלים',
        'titleEn': 'Construction Input Index Linkage: The Silent Price Escalation in Off-Plan Contracts',
        'descHe': 'איך עובד מנגנון ההצמדה בחוזי קבלן, ומה ניתן (וכדאי) לנסות לשנות במשא ומתן.',
        'descEn': 'How the index linkage mechanism works in developer contracts, and what terms you should negotiate to reduce costs.',
        'contentHe': """
            <p>בעת חתימה על חוזה לרכישת דירה מקבלן, המחיר הנקוב בחוזה כמעט אף פעם אינו המחיר הסופי שתשלמו בפועל. אחד הגורמים המרכזיים לייקור הדירה הוא מנגנון ההצמדה למדד תשומות הבנייה, שעלול להוסיף עשרות אלפי שקלים לעלות העסקה.</p>
            
            <h2>מהו מדריך תשומות הבנייה?</h2>
            <p>מדד תשומות הבנייה מפורסם מדי חודש על ידי הלשכה המרכזית לסטטיסטיקה ומשקף את השינויים בעלויות של חומרי הבנייה (מלט, ברזל, בטון), עלויות השכר של הפועלים והובלות. בחוזי קבלן, מקובל להצמיד את יתרת התשלומים שטרם שולמו למדד זה, כדי להגן על הקבלן מפני עליית מחירים פתאומית במהלך תקופת הבנייה.</p>
            
            <h2>התיקון החדש לחוק המכר: הגבלת ההצמדה ל-40% בלבד</h2>
            <p>בעקבות תיקון חשוב לחוק המכר שנכנס לתוקף בשנים האחרונות, חל איסור להצמיד את מלוא מחיר הדירה למדד. כיום, הקבלן רשאי להצמיד לכל היותר 40% ממחיר הדירה למדד תשומות הבנייה, כאשר יתרת ה-60% נותרת קבועה ללא הצמדה. שינוי חקיקתי זה הפחית משמעותית את חשיפת הרוכשים לתנודות המדד, אך עדיין מדובר בעלויות מצטברות ניכרות שיש לקחת בחשבון.</p>
            
            <h2>כיצד ניתן לצמצם את עלויות ההצמדה במשא ומתן?</h2>
            <p>עורך דין מנוסה מטעמכם יפעל לצמצום חשיפתכם למדד באמצעות מספר אסטרטגיות: 1. קביעת מועד מדד בסיס עדכני (למשל מועד החתימה ולא מועד מוקדם יותר). 2. החלת פטור מהצמדה על תשלומים מסוימים. 3. ניצול האפשרות להקדים תשלומים לקבלן (בכפוף לקבלת ערבויות מתאימות) כדי לעצור את צבירת ההצמדה על אותם סכומים.</p>
        """,
        'contentEn': """
            <p>When purchasing an off-plan apartment, the contract price is rarely the final amount paid. One of the main factors driving up final costs is the Construction Input Index linkage, which can add tens of thousands of Shekels.</p>
            
            <h2>What is the Construction Input Index?</h2>
            <p>Published monthly by the Central Bureau of Statistics, this index reflects changes in the costs of building materials (cement, iron), labor, and shipping. Developers link unpaid installation balances to this index to shield themselves from material cost spikes.</p>
            
            <h2>The Sale Law Amendment: Limiting Linkage to 40%</h2>
            <p>Following an important legal reform, developers are prohibited from linking the entire apartment price to the index. Today, only a maximum of 40% of the property value can be linked, while the remaining 60% remains fixed. This limits buyer exposure but still allows for substantial extra costs.</p>
            
            <h2>How to Negotiate and Minimize Index Linkage?</h2>
            <p>Your attorney will employ several strategies to mitigate indexation exposure: 1. Setting the latest baseline index (the contract signing month instead of earlier calls). 2. Exempting specific installments from linkage. 3. Prepaying balances (secured by bank guarantees) to freeze indexation on those amounts.</p>
        """
    },
    {
        'slug': 'contractor-delivery-delay-compensation',
        'practiceAreaId': 'new-contractor-purchase',
        'image': 'article_contractor_3.png',
        'date': '01.06.2026',
        'readTime': '4 min read',
        'categoryHe': 'רכישה מקבלן',
        'categoryEn': 'New Contractor Purchase',
        'titleHe': 'איחור במסירת דירה מקבלן: מתי מגיע לכם פיצוי, וכמה?',
        'titleEn': 'Delayed Apartment Delivery: When Are You Entitled to Compensation?',
        'descHe': 'הוראות החוק לעניין פיצוי בגין איחור במסירה, החריגים שקבלנים נוהגים להכניס לחוזה, ואיך מתמודדים איתם.',
        'descEn': 'Zoning rules for delayed possession, standard developer exceptions built into contracts, and how to assert your rights.',
        'contentHe': """
            <p>איחור במסירת מפתח הוא אחד התרחישים המתסכלים ביותר עבור רוכשי דירה חדשה. הרוכשים נאלצים להמשיך לשלם שכר דירה בדירתם הנוכחית במקביל לתשלומי משכנתא, ולהתמודד עם חוסר ודאות תכנוני ואישי. חוק המכר (דירות) מסדיר נושא זה ומעניק לרוכשים זכות לפיצוי כספי אוטומטי.</p>
            
            <h2>תקופת הגרייס והזכות לפיצוי רטרואקטיבי</h2>
            <p>על פי החוק, לקבלן מותרת תקופת איחור של עד 60 ימים ממועד המסירה החוזי ללא תשלום פיצוי (תקופת גרייס). אולם, במידה והאיחור נמשך מעבר ל-60 ימים, על הקבלן לשלם לרוכש פיצוי כספי רטרואקטיבי החל מהיום הראשון של האיחור, ללא צורך בהוכחת נזק כלשהו.</p>
            
            <h2>גובה הפיצוי על פי החוק</h2>
            <p>החוק קובע נוסחת פיצוי מטיבה המבוססת על שווי שכר דירה של דירה דומה בגודלה ובמיקומה:
            1. עבור שמונת החודשים הראשונים של האיחור: פיצוי חודשי בגובה **150%** (פי 1.5) מדמי השכירות המקובלים בשוק.
            2. החל מהחודש התשיעי ואילך: פיצוי בגובה **125%** מדמי השכירות המקובלים.
            פיצוי זה משולם מדי חודש בחודשו עבור החודש שחלף.</p>
            
            <h2>ניסיונות הקבלנים לעקוף את החוק ("כוח עליון")</h2>
            <p>קבלנים רבים נוהגים להכניס לחוזה סעיפים המפטירים אותם מתשלום פיצוי במקרה של עיכובים הנובעים מנסיבות שאינן בשליטתם (מלחמה, שביתות, מחסור בפועלים, עיכובי עירייה). אולם, בתי המשפט נוקטים עמדה קשוחה מאוד ומפרשים סעיפים אלו בצמצום רב. הקבלן אינו יכול להסתתר מאחורי טענות "כוח עליון" כלליות, אלא עליו להוכיח כי פעל בשקידה סבירה וכי מדובר באירוע חריג ובלתי צפוי לחלוטין שלא ניתן היה למנוע את השפעתו.</p>
        """,
        'contentEn': """
            <p>Late delivery of a new apartment is highly frustrating for buyers, who must bear double housing expenses (rent and mortgages). The Sale Law provides structured rights for automated financial compensation.</p>
            
            <h2>The Grace Period and Retroactive Compensation</h2>
            <p>Under the law, developers have a 60-day grace period beyond the contractual delivery date. However, if the delay exceeds 60 days, the developer must pay compensation retroactively starting from day one of the delay.</p>
            
            <h2>Calculating the Statutory Compensation</h2>
            <p>The law mandates compensation based on the market rent of a comparable apartment in the same area:
            1. For the first 8 months of delay: Monthly payment equal to **150%** of market rent.
            2. From the 9th month onward: Monthly payment equal to **125%** of market rent.</p>
            
            <h2>Developer Attempts to Bypass Liability ("Force Majeure")</h2>
            <p>Developers often insert broad clauses exempting them from delays caused by events beyond their control (labor shortages, municipal delays, wars). However, courts interpret these clauses very restrictively, holding developers liable unless they prove diligent preventive actions.</p>
        """
    },
    # --- Category 3: Urban Renewal ---
    {
        'slug': 'pinui-binui-essential-clauses',
        'practiceAreaId': 'urban-renewal',
        'image': 'article_urban_1.png',
        'date': '29.05.2026',
        'readTime': '6 min read',
        'categoryHe': 'התחדשות עירונית',
        'categoryEn': 'Urban Renewal',
        'titleHe': 'בעלי דירות בפרויקט פינוי-בינוי: עשרת הסעיפים שחייבים להופיע בהסכם מול היזם',
        'titleEn': 'Apartment Owners in Pinui-Binui: 10 Essential Clauses in the Developer Agreement',
        'descHe': 'ערבויות, שכר דירה בתקופת הביניים, מפרט הדירה החדשה ומנגנוני פיקוח — מה שמגן עליכם באמת.',
        'descEn': 'Guarantees, rental subsidies during construction, technical specifications, and supervision mechanisms protecting owners.',
        'contentHe': """
            <p>פרויקט פינוי-בינוי הוא עסקה מורכבת שבה בעלי דירות בבניין ישן מוסרים את נכסיהם להריסה תמורת קבלת דירה חדשה, רחבה וממוגנת בעתיד. כדי להבטיח את זכויותיכם ולמנוע מצב של אובדן הנכס, ההסכם מול היזם חייב לכלול מספר סעיפי מפתח קריטיים.</p>
            
            <h2>1. ערבויות ובטוחות חזקות</h2>
            <p>הבטוחה החשובה ביותר היא **ערבות חוק מכר בשווי הדירה החדשה**, הנמסרת לכל דייר לפני הריסת הבניין הקיים. בנוסף, על היזם להמציא ערבות בנקאית אוטונומית להבטחת תשלום דמי השכירות בתקופת הבנייה, ערבות מסים לכיסוי היבטי מיסוי (שבח, היטל השבחה), וערבות בדק לתיקון ליקויים בדירה החדשה.</p>
            
            <h2>2. מימון דמי שכירות והוצאות מעבר</h2>
            <p>על היזם לשלם לבעלי הדירות דמי שכירות חודשיים ריאליים המאפשרים לשכור דירה חלופית באותה רמה ובאותו אזור לאורך כל תקופת הפרויקט (מחתימה ועד מסירת המפתח). דמי השכירות יתעדכנו לפי מנגנון הצמדה מוסכם. בנוסף, על היזם לממן באופן מלא את הוצאות ההובלה של תכולת הדירה הלוך וחזור.</p>
            
            <h2>3. לוחות זמנים ומפרט טכני עשיר</h2>
            <p>ההסכם חייב להגדיר תאריכי יעד מדויקים לביצוע כל שלב בפרויקט (הגשת תוכניות, קבלת היתר בנייה, תחילת עבודות, מסירת דירות) עם סנקציות כספיות משמעותיות במקרה של איחור. כמו כן, יש לצרף להסכם מפרט טכני מפורט של הדירה החדשה (מפרט חוק מכר) הכולל את גודל הדירה, קומה, כיווני אוויר, חנייה, מחסן, סוגי ריצוף וחיפויים.</p>
        """,
        'contentEn': """
            <p>A Pinui-Binui project is a complex deal where owners surrender old apartments for demolition in exchange for new ones. To protect your rights and avoid loss of property, the developer contract must contain key clauses.</p>
            
            <h2>1. Strong Guarantees and Collateral</h2>
            <p>The most important safeguard is a **Sale Law Bank Guarantee representing the value of the new apartment**, delivered before demolition. The developer must also provide an autonomous rental guarantee, tax guarantees, and a structural warranty bank guarantee.</p>
            
            <h2>2. Rental Subsidies and Relocation Costs</h2>
            <p>Developers must pay realistic monthly rent allowing owners to lease comparable apartments in the same area during construction. In addition, the developer must fully fund moving expenses both ways.</p>
            
            <h2>3. Precise Timelines and Technical Specifications</h2>
            <p>The contract must set exact milestones (permitting, demolition, construction, delivery) with financial penalties for delays. Detailed technical blueprints for the new apartments (finishes, storage, parking) must be annexed.</p>
        """
    },
    {
        'slug': 'urban-renewal-homeowners-committee',
        'practiceAreaId': 'urban-renewal',
        'image': 'article_urban_2.png',
        'date': '25.05.2026',
        'readTime': '5 min read',
        'categoryHe': 'התחדשות עירונית',
        'categoryEn': 'Urban Renewal',
        'titleHe': 'נציגות הבית המשותף בהתחדשות עירונית: סמכויות, אחריות וניגודי עניינים',
        'titleEn': 'Condominium Representations in Urban Renewal: Authority and Conflicts of Interest',
        'descHe': 'איך בוחרים נציגות, מה מותר ואסור לה להחליט בשם הדיירים, ולמה ליווי משפטי עצמאי הוא תנאי בל-יעבור.',
        'descEn': 'How to choose a homeowners committee, their legal limits, and why independent legal representation is a non-negotiable requirement.',
        'contentHe': """
            <p>נציגות הדיירים (הבית המשותף) ממלאת תפקיד מפתח בהצלחת פרויקטים של התחדשות עירונית (תמ"א 38 או פינוי בינוי). היא משמשת כחוליה המקשרת בין בעלי הדירות לבין היזם, עורכי הדין ואנשי המקצוע. עם זאת, פעילות הנציגות מעלה שאלות רבות לגבי גבולות סמכותה וחששות מניגודי עניינים.</p>
            
            <h2>כיצד בוחרים נציגות דיירים כחוק?</h2>
            <p>בחירת הנציגות חייבת להתבצע במסגרת אסיפת דיירים כללית של כלל בעלי הדירות בבניין. יש לפרסם הודעה מראש על האסיפה ולנהל פרוטוקול מסודר שבו ירשמו שמות חברי הנציגות שנבחרו ברוב קולות. נציגות שלא נבחרה כדין אינה מוסמכת לייצג את הדיירים, וחתימותיה או החלטותיה עלולות להיפסל בהמשך הדרך.</p>
            
            <h2>סמכויות הנציגות: ייצוג בלבד, לא קבלת החלטות מהותיות</h2>
            <p>חשוב להבין כי תפקיד הנציגות הוא **ניהול המשא ומתן המקדמי וייצוג הדיירים**, ואין לה סמכות משפטית לקבל החלטות קנייניות מהותיות בשם אף דייר. הנציגות אינה יכולה לקבוע מי יהיה היזם ללא אישור האסיפה, ואינה יכולה לחתום על הסכם סופי בשם בעל דירה אחר. כל דייר חייב לחתום באופן אישי על חוזה המכר מול היזם.</p>
            
            <h2>מניעת ניגודי עניינים והבטחת שקיפות</h2>
            <p>אחד החששות הגדולים ביותר של דיירים הוא שחברי הנציגות יקבלו "טובות הנאה" סמויות מהיזם בתמורה לקידום הפרויקט. כדי למנוע זאת, יש להחתים את חברי הנציגות על הצהרת היעדר ניגוד עניינים, לקבוע חובת דיווח ושקיפות מלאה על כל פגישה או הצעה, ולהבטיח שליווי עורכי הדין של הדיירים ממומן על ידי היזם אך כפוף ומחויב אך ורק לאינטרסים של בעלי הדירות.</p>
        """,
        'contentEn': """
            <p>The homeowners committee plays a key role in Urban Renewal. Serving as the link between owners and developers, their operations raise questions regarding authority limits and conflicts of interest.</p>
            
            <h2>How to Lawfully Elect a Homeowners Committee?</h2>
            <p>The election must occur during a general meeting of all property owners. Proper minutes recording the majority votes electing members must be kept. An improperly elected committee holds no authority to represent owners.</p>
            
            <h2>Committee Authority: Representation, Not Decision-Making</h2>
            <p>The committee is tasked with **preliminary negotiations and representation**, and holds no legal authority to make proprietary decisions. They cannot sign the final binding agreement on behalf of other owners.</p>
            
            <h2>Preventing Conflicts of Interest and Assuring Transparency</h2>
            <p>To prevent members from receiving unauthorized benefits from developers, they must sign a conflict of interest waiver, report all developer meetings, and ensure the owners\' attorney is loyal strictly to the residents.</p>
        """
    },
    {
        'slug': 'tma-38-choosing-developer',
        'practiceAreaId': 'urban-renewal',
        'image': 'article_urban_3.png',
        'date': '20.05.2026',
        'readTime': '5 min read',
        'categoryHe': 'התחדשות עירונית',
        'categoryEn': 'Urban Renewal',
        'titleHe': 'איך בוחרים יזם לפרויקט תמ"א 38 — מדריך לעריכת מכרז יזמים נכון',
        'titleEn': 'Choosing a Developer for TMA 38: A Guide to Running a Tender',
        'descHe': 'קריטריונים לבחינת חוסן פיננסי וניסיון, והדרך הנכונה להשוות בין הצעות מעבר ל"כמה מטרים מקבלים".',
        'descEn': 'Criteria for assessing financial stability and track records, and the correct way to compare commercial bids.',
        'contentHe': """
            <p>בחירת היזם לפרויקט תמ"א 38 (חיזוק ותוספת או הריסה ובנייה) היא ההחלטה הגורלית ביותר שבעלי הדירות נדרשים לקבל. שוק ההתחדשות העירונית רווי בחברות קבלניות ויזמיות, והדרך הטובה ביותר לבחור את השותף המתאים היא באמצעות ביצוע מכרז יזמים תחרותי ומקצועי.</p>
            
            <h2>1. הכנת מסמך פנייה לקבלת הצעות (RFP)</h2>
            <p>המכרז מתחיל בהכנת מסמך פניות מפורט על ידי עורך הדין והמפקח של הדיירים. מסמך זה מגדיר את תנאי הסף שעל היזמים לעמוד בהם, את דרישות המינימום של הדיירים (תוספת מטרים, מרפסת, חנייה, מפרט טכני) ואת האופן שבו יש להגיש את ההצעות. הגשת מסמך אחיד מאפשרת להשוות בין ההצעות השונות "תפוחים לתפוחים".</p>
            
            <h2>2. בחינת חוסן פיננסי וניסיון מוכח בשטח</h2>
            <p>מעבר להבטחות שיווקיות, יש לבדוק שני פרמטרים מרכזיים:
            * **ניסיון ביצועי**: כמה פרויקטים של תמ"א 38 היזם כבר השלים בהצלחה ומסר לדיירים (יש לבקר באותם בניינים ולשוחח עם נציגויות הדיירים שם).
            * **חוסן פיננסי**: יכולתו של היזם להעמיד ערבויות בנקאיות אוטונומיות מחמירות מחוק המכר, והקשרים שלו עם בנקים מלווים מובילים בישראל.</p>
            
            <h2>3. השוואת תמורות מסחריות ועיגון מנגנוני ביטחון</h2>
            <p>במכרז מקצועי, בעלי הדירות לא מתפתים להצעה הגבוהה ביותר על הנייר (למשל תוספת מטרים לא ריאלית שהעירייה לא תאשר). השמאי והמפקח מטעם הדיירים יבחנו את היתכנות התמורות, ויזם יבחר לא רק לפי מטרים, אלא לפי איכות המפרט הטכני, גובה הערבויות, מקצועיות הצוות התכנוני ונכונותו לעגן בהסכם סעיפי סנקציות נוקשים במקרה של עיכובים.</p>
        """,
        'contentEn': """
            <p>Choosing the developer for your TMA 38 project is the most critical decision homeowners must make. The best way to select the right partner is by conducting a professional, competitive developer tender.</p>
            
            <h2>1. Preparing the Request for Proposals (RFP)</h2>
            <p>The tender begins with a detailed RFP prepared by the owners\' attorney and supervisor, setting threshold criteria (required apartment extensions, balconies, parking, and baseline finishes) to compare bids fairly.</p>
            
            <h2>2. Assessing Financial Stability and Completed Projects</h2>
            <p>Beyond sales presentations, check two factors:
            * **Track Record**: How many TMA 38 projects has the developer successfully completed? (Visit completed sites and speak with residents).
            * **Financial Capacity**: Can the developer secure bank guarantees?</p>
            
            <h2>3. Comparing Commercial Offers and Safety Nets</h2>
            <p>Homeowners should not simply choose the highest paper offer (which might be rejected by planners). Analyze construction specifications, guarantee sizes, and the developer\'s willingness to agree to delay penalties.</p>
        """
    },
    # --- Category 4: Real Estate Taxation ---
    {
        'slug': 'capital-gains-tax-exemptions',
        'practiceAreaId': 'real-estate-taxation',
        'image': 'article_tax_1.png',
        'date': '15.05.2026',
        'readTime': '5 min read',
        'categoryHe': 'מיסוי מקרקעין',
        'categoryEn': 'Real Estate Taxation',
        'titleHe': 'מס שבח במכירת דירה: הפטורים שכדאי להכיר לפני שחותמים',
        'titleEn': 'Capital Gains Tax (Mas Shevach): Exemptions to Know Before Selling',
        'descHe': 'פטור דירה יחידה, הוראות מעבר, ותרחישים נפוצים שבהם תכנון מוקדם חוסך סכומים משמעותיים.',
        'descEn': 'Single residential exemptions, transitional provisions, and common scenarios where tax planning saves major sums.',
        'contentHe': """
            <p>מכירת דירת מגורים בישראל כרוכה לרוב בחבות במס שבח — מס המוטל על רווח ההון שנוצר למוכר מהפרש המחירים בין מועד הרכישה למועד המכירה. שיעור המס עומד על 25% מהרווח הריאלי, אך חוק מיסוי מקרקעין כולל מגוון פטורים שיכולים לאפס לחלוטין את חבות המס.</p>
            
            <h2>1. פטור דירת מגורים יחידה מזכה</h2>
            <p>זהו הפטור הנפוץ והמשמעותי ביותר. מוכר זכאי לפטור מלא ממס שבח בגין מכירת דירתו היחידה, בתנאי שהיה בעל הדירה במשך 18 חודשים לפחות מיום סיום הבנייה, והוא לא מכר דירה אחרת בפטור זה במהלך 18 החודשים שקדמו למכירה. החוק מגדיר "דירה יחידה" גם במצבים שבהם למוכר יש חלק קטן בדירה נוספת (עד שליש) או דירה שהתקבלה בירושה תחת תנאים מסוימים.</p>
            
            <h2>2. פטור דירה שהתקבלה בירושה</h2>
            <p>יורש של דירת מגורים עשוי להיות זכאי לפטור ממס שבח בעת מכירתה, גם אם יש בבעלותו דירות נוספות. כדי לקבל את הפטור, על המוכר לעמוד בשלושה תנאים מצטברים: 1. המוכר הוא בן זוגו של המוריש, או צאצא שלו (ילד/נכד). 2. לפני פטירתו, המוריש היה בעלים של דירת מגורים אחת בלבד. 3. אילו המוריש היה עדיין בחיים ומוכר את הדירה, הוא היה זכאי לפטור ממס שבח.</p>
            
            <h2>3. חישוב ליניארי מוטב (הפרדת מס לפי שנים)</h2>
            <p>עבור מוכרים שאינם זכאים לפטור מלא (למשל בעלי מספר דירות להשקעה), קיים מנגנון המכונה "חישוב ליניארי מוטב". מנגנון זה מעניק פטור ממס שבח על החלק היחסי של השבח שנצבר עד ליום 1 בינואר 2014, ומטיל מס של 25% רק על יתרת השבח שנצברה לאחר תאריך זה. תכנון מס מדויק מאפשר להפחית עשרות אלפי שקלים מהמס המבוקש על ידי רשויות המס.</p>
        """,
        'contentEn': """
            <p>Selling a residential property in Israel involves Capital Gains Tax (Mas Shevach) representing 25% of the real profit. However, tax laws offer several exemptions that can lower this tax liability to zero.</p>
            
            <h2>1. The Single Residential Home Exemption</h2>
            <p>This is the most common exemption. A seller is exempt from tax when selling their sole residential home, provided they owned it for at least 18 months prior to the sale and have not utilized this exemption in the preceding 18 months.</p>
            
            <h2>2. Inherited Property Exemption</h2>
            <p>An heir of a residential property may be exempt from capital gains tax upon its sale, even if they own other properties, provided they are a direct descendant or spouse, the deceased owned only one home, and the deceased would have been exempt if alive.</p>
            
            <h2>3. The Beneficiary Linear Calculation</h2>
            <p>For sellers who do not qualify for a full exemption (e.g. investors), the pro-rata linear method taxes gains accumulated only after January 1, 2014, exempting any gains accrued before that date.</p>
        """
    },
    {
        'slug': 'purchase-tax-brackets-2026',
        'practiceAreaId': 'real-estate-taxation',
        'image': 'article_tax_2.png',
        'date': '10.05.2026',
        'readTime': '4 min read',
        'categoryHe': 'מיסוי מקרקעין',
        'categoryEn': 'Real Estate Taxation',
        'titleHe': 'מס רכישה 2026: מדרגות, הקלות וזכאויות שרוכשים לא תמיד מנצלים',
        'titleEn': 'Purchase Tax (Mas Rechisha) 2026: Brackets, Reliefs and Underutilized Exemptions',
        'descHe': 'מדרגות המס העדכניות, ההבדל בין דירה יחידה לדירה נוספת, והקלות לעולים, לנכים ולמשפרי דיור.',
        'descEn': 'Updated tax brackets, differences between single and additional properties, and reliefs for Olim, disabled buyers, and home upgraders.',
        'contentHe': """
            <p>רכישת דירת מגורים בישראל מפעילה חבות בתשלום מס רכישה — מס מדורג המשולם על ידי הקונה בתוך 60 ימים ממועד העסקה. גובה המס ומדרגותיו משתנים מדי שנה (בחודש ינואר) ומבוססים על מדד מחירי הדירות. תכנון נכון וזיהוי הקלות יכולים לחסוך סכומי כסף משמעותיים.</p>
            
            <h2>מדרגות מס רכישה לשנת 2026 (לרוכשי דירה יחידה)</h2>
            <p>נכון לשנת 2026, רוכשי דירת מגורים יחידה זכאים לפטור מלא ממס על שווי הנכס של עד כ-1,970,000 ש"ח. מעבר לסכום זה חלות מדרגות מס מדורגות:
            * משווי של 1,970,000 ש"ח ועד 2,340,000 ש"ח — 3.5% מס.
            * משווי של 2,340,000 ש"ח ועד 3,000,000 ש"ח — 5% מס.
            * משווי של 3,000,000 ש"ח ועד 5,300,000 ש"ח — 8% מס.
            * משווי מעל 5,300,000 ש"ח — 10% מס.</p>
            
            <h2>מדרגות מס רכישה לדירה נוספת (משקיעים)</h2>
            <p>עבור רוכשים שבבעלותם דירה נוספת, החוק מטיל מס רכישה מהשקל הראשון של העסקה ללא פטורים:
            * משווי של עד כ-6,050,000 ש"ח — 8% מס רכישה.
            * על חלק השווי העולה על סכום זה — 10% מס רכישה.</p>
            
            <h2>הקלות ופטורים מיוחדים שחשוב להכיר</h2>
            <p>החוק מעניק הקלות משמעותיות לאוכלוסיות מוגדרות:
            1. **עולים חדשים**: זכאים לשיעור מס מופחת של 0.5% (או פטור מלא עד תקרות מסוימות) ברכישת דירת מגורים או עסק בתוך 7 שנים מיום עלייתם.
            2. **נכים, עיוורים ונפגעי פעולות איבה**: זכאים לשיעור מס מופחת של 0.5% ברכישת דירת מגורים המיועדת למגוריהם.
            3. **משפרי דיור**: רוכש דירה שנייה שמתחייב למכור את דירתו הראשונה בתוך 18 חודשים, ייחשב כרוכש דירה יחידה וייהנה מהפטור וממדרגות המס המקלות.</p>
        """,
        'contentEn': """
            <p>Purchasing residential property in Israel triggers Purchase Tax (Mas Rechisha) which must be paid by the buyer within 60 days of the deal. Brackets are updated annually in January based on real estate indices.</p>
            
            <h2>Purchase Tax Brackets 2026 (Single Residential Home)</h2>
            <p>In 2026, buyers of a single residential property enjoy a complete tax exemption on values up to approximately 1,970,000 NIS. Above this threshold, progressive brackets apply: 3.5%, 5%, 8%, and 10%.</p>
            
            <h2>Purchase Tax for Additional Properties (Investors)</h2>
            <p>For buyers acquiring additional homes, tax is charged from the first Shekel:
            * Up to approximately 6,050,000 NIS — 8% tax.
            * Above this value — 10% tax.</p>
            
            <h2>Underutilized Reliefs and Special Exemptions</h2>
            <p>Significant tax discounts are available for specific groups:
            1. **Olim Hadashim (New Immigrants)**: Eligible for a reduced tax rate of 0.5% (or full exemptions up to thresholds) within 7 years of Aliyah.
            2. **Disabled Buyers & Terror Victims**: Entitled to a reduced rate of 0.5% for residential purchases.
            3. **Home Upgraders**: Buying a second home while committing to sell the first within 18 months allows paying single-home rates.</p>
        """
    },
    {
        'slug': 'betterment-levy-guide',
        'practiceAreaId': 'real-estate-taxation',
        'image': 'article_tax_3.png',
        'date': '05.05.2026',
        'readTime': '4 min read',
        'categoryHe': 'מיסוי מקרקעין',
        'categoryEn': 'Real Estate Taxation',
        'titleHe': 'היטל השבחה — מתי הוא חל, איך מחושב, ואיך משיגים על השומה',
        'titleEn': 'Betterment Levy (Heitel Hashbacha): Triggers, Calculations, and Objections',
        'descHe': 'ההבדל בין היטל השבחה למס שבח, מועד החיוב, ומסלולי השגה והערר על שומת הוועדה המקומית.',
        'descEn': 'The difference between betterment levy and capital gains tax, payment triggers, and administrative appeals processes.',
        'contentHe': """
            <p>היטל השבחה הוא תשלום חובה הנדרש על ידי הוועדה המקומית לתכנון ובנייה מבעלי מקרקעין, בגין עליית שווי הנכס שלהם עקב אישור תוכנית מתאר מקומית (תב"ע), אישור הקלה או אישור שימוש חורג. בעסקאות רבות, מדובר בדרישות תשלום של עשרות או מאות אלפי שקלים המפתיעות את המוכרים.</p>
            
            <h2>ההבדל בין היטל השבחה למס שבח</h2>
            <p>רבים נוטים להתבלבל בין שני המסים הללו, אך מדובר בתשלומים שונים לחלוטין:
            * **מס שבח**: משולם לרשות המסים הארצית (משרד האוצר) בגין רווח ההון שנוצר מעליית שווי השוק של הנכס.
            * **היטל השבחה**: משולם לרשות המקומית (העירייה) בגין השבחה תכנונית (הגדלת זכויות בנייה, שינוי ייעוד מקרקע חקלאית למגורים וכדומה).</p>
            
            <h2>מתי חלה חובת התשלום בפועל?</h2>
            <p>ההשבחה עצמה מתרחשת במועד אישור התוכנית המשביחה, אך חובת התשלום נדחית למועד "מימוש הזכויות" בנכס. מימוש זכויות מוגדר בעיקר כחתימה על חוזה למכירת הנכס (העברת בעלות) או הגשת בקשה לקבלת היתר בנייה בפועל לניצול זכויות הבנייה שנוספו.</p>
            
            <h2>כיצד משיגים על גובה שומת היטל ההשבחה?</h2>
            <p>עם קבלת דרישת התשלום (השומה) מהוועדה המקומית, עומדת לבעל הנכס זכות להגיש ערעור בתוך 45 ימים. ההליכים מבוצעים בשני מסלולים עיקריים:
            1. **שמאי מכריע**: הגשת בקשה למינוי שמאי מקרקעין ניטרלי מטעם משרד המשפטים לבחינת השומה והכרעה במחלוקת.
            2. **ועדת ערר לפיצויים והיטלי השבחה**: הגשת ערעור משפטי במקרים שבהם המחלוקת היא משפטית (כגון שאלת עצם החבות בהיטל או זכאות לפטורים חוקיים כגון פטור בגין בניית ממ"ד או הרחבת דירת מגורים).</p>
        """,
        'contentEn': """
            <p>A Betterment Levy (Heitel Hashbacha) is a charge imposed by local planning committees on property owners when a new local zoning plan, planning easement, or non-conforming use permit increases their property\'s value.</p>
            
            <h2>Betterment Levy vs. Capital Gains Tax</h2>
            <p>These two taxes are often confused but are entirely distinct:
            * **Mas Shevach**: Paid to the National Tax Authority based on financial market profit upon sale.
            * **Heitel Hashbacha**: Paid to the local municipality based on planning improvements (such as expanded building rights).</p>
            
            <h2>When is the Betterment Levy Actually Payable?</h2>
            <p>The levy obligation is triggered when the zoning plan is approved, but the payment is deferred until "realization of rights" – typically when selling the property or applying for a building permit.</p>
            
            <h2>How to Appeal a Betterment Levy Assessment?</h2>
            <p>Upon receiving the assessment from the local committee, owners have 45 days to appeal via two channels:
            1. **Decisive Appraiser (Shamai Machria)**: Requesting an independent appraiser from the Ministry of Justice to rule on the valuation.
            2. **Appeals Committee**: Filing a legal appeal regarding statutory liability exemptions (such as Mamad exemptions).</p>
        """
    },
    # --- Category 5: Commercial Properties ---
    {
        'slug': 'commercial-lease-agreement-tips',
        'practiceAreaId': 'commercial-properties',
        'image': 'article_commercial_1.png',
        'date': '29.04.2026',
        'readTime': '5 min read',
        'categoryHe': 'נדל״ן מסחרי',
        'categoryEn': 'Commercial Properties',
        'titleHe': 'הסכם שכירות מסחרית: הסעיפים הקריטיים שמכריעים את גורל העסק שלכם',
        'titleEn': 'Commercial Lease Agreements: Critical Clauses That Shape Your Business Future',
        'descHe': 'תקופות אופציה, מנגנוני עדכון דמי שכירות, ערבויות ופינוי — ממבט המשכיר וממבט השוכר.',
        'descEn': 'Option periods, rent escalation indexes, bank guarantees, and exit clauses from both landlord and tenant perspectives.',
        'contentHe': """
            <p>בניגוד להסכמי שכירות למגורים, הסכמי שכירות מסחרית (חנויות, משרדים, תעשייה) הם חוזים מורכבים ביותר שאינם כפופים לחוקי הגנת הצרכן המקובלים. חוזים אלו נחתמים לרוב לתקופות ארוכות טווח ומערבים השקעות כספיות משמעותיות, ולכן כל סעיף בהם עשוי להכריע את כדאיות העסק.</p>
            
            <h2>1. תקופת השכירות והאופציה להארכה</h2>
            <p>הסעיף החשוב ביותר עבור שוכר מסחרי הוא קבלת תקופת אופציה להארכת החוזה. השוכר משקיע ממון רב בהתאמת המושכר ובבניית מוניטין במיקום הספציפי, ועל כן עליו לוודא כי תנתן לו הזכות להאריך את תקופת השכירות למספר שנים נוספות ללא חשש מפינוי שרירותי. מנגד, על המשכיר לקבוע תנאים ברורים למימוש האופציה (כגון היעדר הפרות חוזה והודעה מראש בכתב).</p>
            
            <h2>2. מנגנון עדכון דמי השכירות</h2>
            <p>בשכירות ארוכת טווח, מקובל לקבוע מנגנון להעלאת דמי השכירות בתקופת האופציה (בדרך כלל עלייה של 5% עד 10% בהשוואה לתקופת הבסיס). יש לוודא כי מנגנון העדכון ברור וחד-משמעי, וכי דמי השכירות צמודים למדד המחירים לצרכן בצורה הוגנת המונעת זינוקים בלתי צפויים בעלויות הקבועות של העסק.</p>
            
            <h2>3. חלוקת האחריות לשיפוצים ותשתיות</h2>
            <p>נושא שכיח לסכסוכים הוא חלוקת האחריות לתיקונים במושכר. ככלל, נהוג לקבוע כי המשכיר אחראי לתיקון בלאי סביר במערכות הבניין הראשיות (קונסטרוקציה, איטום גגות, מערכות כיבוי אש ראשיות), בעוד השוכר נושא באחריות לתחזוקה השוטפת ולמערכות הפנימיות שהתקין (מיזוג אוויר פנימי, אינסטלציה פנימית, חיפויים).</p>
        """,
        'contentEn': """
            <p>Unlike residential rentals, commercial leases (for retail, offices, industrial spaces) are highly complex, long-term contracts. Because they involve substantial capital investments, every single clause is critical.</p>
            
            <h2>1. Lease Terms and Renewal Options</h2>
            <p>Securing a renewal option is crucial for commercial tenants who invest heavily in fit-outs. Landlords, conversely, require clear conditions for exercising options, such as absence of prior breaches and timely written notices.</p>
            
            <h2>2. Rent Escalation and Indexation</h2>
            <p>In long-term leases, it is standard to increase rent during option periods (typically by 5% to 10%). Both parties must ensure the price adjustment formulas and Consumer Price Index link parameters are clearly defined.</p>
            
            <h2>3. Maintenance and Structural Repairs</h2>
            <p>A common source of litigation is repair liability. Typically, landlords cover structural repairs (roof sealing, foundations) while tenants maintain interior infrastructure (internal AC units, wiring, plumbing).</p>
        """
    },
    {
        'slug': 'yield-property-due-diligence',
        'practiceAreaId': 'commercial-properties',
        'image': 'article_commercial_2.png',
        'date': '20.04.2026',
        'readTime': '5 min read',
        'categoryHe': 'נדל״ן מסחרי',
        'categoryEn': 'Commercial Properties',
        'titleHe': 'רכישת נכס מניב כהשקעה: בדיקת נאותות משפטית שמעבר לתשואה',
        'titleEn': 'Buying Yield-Generating Property: Legal Due Diligence Beyond the Cap Rate',
        'descHe': 'מה בודקים בהסכמי השכירות הקיימים, ברישוי העסק ובזכויות התכנוניות לפני שמתחייבים.',
        'descEn': 'What to check in existing leases, business licenses, and planning rights before committing capital.',
        'contentHe': """
            <p>רכישת נדל"ן מסחרי מניב (משרדים, מרכזים מסחריים, חנויות רחוב) היא אפיק השקעה פופולרי המציע שיעורי תשואה גבוהים משמעותית משוק המגורים. עם זאת, רכישה כזו מלווה בסיכונים משפטיים ותכנוניים ייחודיים המצריכים עריכת בדיקת נאותות משפטית מקיפה טרם סגירת העסקה.</p>
            
            <h2>1. ניתוח משפטי של הסכמי השכירות הקיימים</h2>
            <p>ערכו הכלכלי של נכס מניב נגזר ישירות מאיכות השוכרים ומחוזק הסכמי השכירות הקיימים. יש לבצע בדיקה מדוקדקת של כל חוזה שכירות פעיל: מהו גובה השכירות בפועל, האם קיימות אופציות הארכה לשוכרים ובאילו תנאים, אילו בטוחות וערבויות (ערבות בנקאית, שטר חוב) מופקדות להבטחת התשלומים, והאם קיימת לשוכרים זכות יציאה מוקדמת העלולה להשאיר את הנכס ריק.</p>
            
            <h2>2. בדיקת היתרי בנייה, רישוי עסקים ושימושים חורגים</h2>
            <p>נכסים מסחריים רבים סובלים מבעיות תכנוניות חמורות. יש לוודא כי השימוש הנוכחי בנכס (למשל, מסעדה או חנות) תואם את היתר הבנייה המקורי ואת תוכנית בניין העיר (תב"ע). הפעלת עסק ללא רישוי מתאים, או בניגוד לייעוד התכנוני המותר, חושפת את בעלי הנכס להליכים פליליים, צווי סגירה וקנסות כבדים מצד הרשות המקומית.</p>
            
            <h2>3. בדיקת שעבודים, חובות והיטלי השבחה</h2>
            <p>יש לבצע בדיקות מקיפות ברשם המשכונות, בטאבו ובעירייה כדי לוודא שאין על הנכס חובות ארנונה או מים היסטוריים, ושעבודים לטובת בנקים או צדדים שלישיים. בדיקה קריטית נוספת היא קיומו של היטל השבחה פוטנציאלי — אישור תוכניות משביחות בעבר עלול להטיל חבות מס משמעותית על המוכר או לעבור לקונה במידה והחוזה לא נוסח נכון.</p>
        """,
        'contentEn': """
            <p>Purchasing yield-generating commercial real estate offers higher yields than the residential market but carries unique legal and planning risks requiring exhaustive due diligence.</p>
            
            <h2>1. Legal Analysis of Active Leases</h2>
            <p>The value of a yield property is tied to lease contracts. You must audit every active lease: verify rent amounts, option terms, bank guarantees, and whether tenants hold early termination clauses.</p>
            
            <h2>2. Building Permits, Zoning, and Business Licensing</h2>
            <p>Many commercial properties face zoning issues. Ensure the current property usage matches building permits. Operating a business without a license exposes owners to closure orders and municipal fines.</p>
            
            <h2>3. Liens, Municipal Debts, and Betterment Levies</h2>
            <p>Run registry checks to verify that the property is clear of municipal tax debts, corporate pledges, or pending betterment levies which could transfer to the buyer if the contract is drafted poorly.</p>
        """
    },
    {
        'slug': 'protected-vs-free-commercial-lease',
        'practiceAreaId': 'commercial-properties',
        'image': 'article_commercial_3.png',
        'date': '10.04.2026',
        'readTime': '5 min read',
        'categoryHe': 'נדל״ן מסחרי',
        'categoryEn': 'Commercial Properties',
        'titleHe': 'שכירות מוגנת מול שכירות חופשית בנכסים מסחריים — מה ההבדל ולמה זה קריטי למחיר',
        'titleEn': 'Protected vs. Free Leases in Commercial Real Estate: Valuation and Exit Impacts',
        'descHe': 'דמי מפתח, דייר מוגן והשלכותיהם על שווי הנכס ועל יכולת הפינוי.',
        'descEn': 'Key differences between key money protection and standard leases, and their impact on property value and eviction rights.',
        'contentHe': """
            <p>בשוק הנדל"ן המסחרי בישראל, בעיקר במרכזי הערים הוותיקים (תל אביב, ירושלים, חיפה), קיימים נכסים רבים הכפופים לחוק הגנת הדייר (שכירות מוגנת או עסקאות "דמי מפתח"). מדובר בשיטה משפטית היסטורית המעניקה לשוכר זכויות חזקות מאוד, ויש לה השפעה דרמטית על מחיר הנכס ועל זכויות הבעלים.</p>
            
            <h2>מהי שכירות מוגנת (דמי מפתח)?</h2>
            <p>שכירות מוגנת היא מערכת יחסים חוזית שבה השוכר משלם סכום ראשוני משמעותי המכונה "דמי מפתח" (בדרך כלל כשליש עד מחצית משווי השוק של הנכס) לבעל הבית, ובתמורה משלם דמי שכירות חודשיים סמליים ונמוכים מאוד לאורך כל תקופת מגוריו או הפעלת העסק בנכס. הדייר המוגן נהנה מחסינות כמעט מוחלטת מפני פינוי, וזכות זו אף ניתנת להעברה ליורשים תחת תנאים מסוימים.</p>
            
            <h2>ההבדלים המרכזיים לעומת שכירות חופשית</h2>
            <p>בעוד שבשכירות חופשית רגילה החוזה נחתם לתקופה קצובה והבעלים יכול לפנות את השוכר או להעלות את דמי השכירות עם סיום החוזה, בשכירות מוגנת:
            * **גובה דמי השכירות**: נקבע על פי תקנות ממשלתיות ואינו משקף את מחירי השוק.
            * **עילות פינוי**: הבעלים יכול לפנות דייר מוגן רק בעילות ספציפיות המוגדרות בחוק (אי-תשלום דמי שכירות, נטישת הנכס, או צורך עצמי של בעל הבית הכרוך במתן דיור חלוף).</p>
            
            <h2>ההשלכות על שווי הנכס ויכולת המימוש</h2>
            <p>קיומו של דייר מוגן בנכס מסחרי מפחית באופן דרמטי את שווי השוק שלו (לעיתים עד 50% או יותר משווי נכס פנוי), שכן הבעלים אינו יכול ליהנות מתזרים מזומנים חופשי או למכור את הנכס כנכס פנוי לשימוש מיידי. בעת רכישת נכס מסחרי, חובה לבדוק את סטטוס השוכרים כדי להימנע מרכישת נכס "נעול" שאינו מאפשר פיתוח או השבחה.</p>
        """,
        'contentEn': """
            <p>In Israel\'s commercial real estate market, especially in historic city centers, many properties are bound by the Tenant Protection Law (Protected Tenancy or "Key Money"). This yields unique rights impacting valuation.</p>
            
            <h2>What is a Protected Lease (Key Money)?</h2>
            <p>Protected tenancy is a legal setup where a tenant pays a substantial upfront lump sum ("Key Money") and in exchange pays very low, regulated monthly rents. Protected tenants enjoy near-total immunity from eviction.</p>
            
            <h2>Key Differences from Free Market Leases</h2>
            <p>While standard leases expire after a set term, protected tenancies:
            * **Rent Rates**: Are determined by government regulations and do not reflect market rates.
            * **Eviction Grounds**: Are limited to statutory reasons (non-payment of rent, abandonment of property).</p>
            
            <h2>Impact on Property Valuation and Realization</h2>
            <p>A protected tenant lowers the market value of a property (often by 50% or more) since the owner cannot rent it at market rate. When buying commercial properties, verify tenant status to avoid "locked" assets.</p>
        """
    },
    # --- Category 6: Partnerships & Co-ownership ---
    {
        'slug': 'coownership-agreement-importance',
        'practiceAreaId': 'partnerships-coownership',
        'image': 'article_partnership_1.png',
        'date': '28.03.2026',
        'readTime': '5 min read',
        'categoryHe': 'הסכמי שיתוף',
        'categoryEn': 'Partnerships & Co-ownership',
        'titleHe': 'הסכם שיתוף במקרקעין: כך מונעים מראש את סכסוך השותפים הבא',
        'titleEn': 'Co-ownership Agreements: Preventing Disputes in Joint Real Estate Ventures',
        'descHe': 'מה מסדירים בהסכם שיתוף — שימוש, נשיאה בהוצאות, מנגנוני הכרעה וזכות סירוב ראשונה — ולמה רישומו בטאבו משנה הכול.',
        'descEn': 'What to regulate in a co-ownership agreement - usage rights, expenses, deadlock resolution, and why registry in Tabu changes everything.',
        'contentHe': """
            <p>שותפות במקרקעין (מושע - נכס הרשום על שם מספר בעלים ללא חלוקה פיזית מוגדרת) היא קרקע פורייה לסכסוכים קשים. מקרים של חילוקי דעות לגבי ניהול הנכס, חלוקת ההוצאות או רצון של אחד השותפים למכור את חלקו, עלולים להוביל להליכים משפטיים יקרים. הדרך היעילה ביותר למנוע זאת מראש היא חתימה על הסכם שיתוף במקרקעין.</p>
            
            <h2>מהו הסכם שיתוף במקרקעין?</h2>
            <p>הסכם שיתוף הוא חוזה משפטי המסדיר את מערכת היחסים בין השותפים בנכס. ההסכם קובע את אופן השימוש הפיזי בנכס (איזה חלק שייך לכל שותף), חלוקת ההכנסות והוצאות התחזוקה, מנגנוני קבלת החלטות ביומיום ומנגנון לפתרון מחלוקות במקרים של מבוי סתום (Deadlock).</p>
            
            <h2>זכות סירוב ראשונה והגבלת עסקאות</h2>
            <p>היבט קריטי בהסכמי שיתוף הוא הסדרת אופן מכירת חלקו של אחד השותפים. נהוג לעגן בהסכם "זכות סירוב ראשונה", המקנה לשותפים הקיימים את הזכות לרכוש את חלקו של השותף המעוניין למכור, באותם תנאים שהוצעו לו על ידי צד שלישי. סעיף זה מונע כניסה של שותפים זרים ולא רצויים לנכס ללא הסכמת יתר השותפים.</p>
            
            <h2>למה חובה לרשום את ההסכם בטאבו?</h2>
            <p>הסכם שיתוף שאינו רשום בטאבו מחייב אך ורק את השותפים שחתמו עליו באופן אישי. כדי להעניק להסכם תוקף קנייני מלא שיחייב גם שותפים עתידיים (כגון קונים שירכשו חלק של אחד השותפים, או יורשים), **חובה לרשום את הסכם השיתוף בלשכת רישום המקרקעין (הטאבו)**. רישום זה הופך את ההסכם לחלק בלתי נפרד ממרשם הנכס הגלוי לכל רוכש פוטנציאלי.</p>
        """,
        'contentEn': """
            <p>Joint ownership of real estate (Mushea - properties registered under multiple owners without physical subdivision) is a common source of disputes. A Co-ownership Agreement is the best preventive tool.</p>
            
            <h2>What is a Co-ownership Agreement?</h2>
            <p>A co-ownership agreement is a contract regulating joint owners. It outlines physical usage rights (which owner gets which area), cost allocation, decision-making, and dispute resolution models.</p>
            
            <h2>Right of First Refusal and Sale Restrictions</h2>
            <p>A critical clause is regulating how an owner sells their share. Agreements typically define a "Right of First Refusal", giving active co-owners the option to buy out the departing partner under market terms.</p>
            
            <h2>Why registering the Agreement in Tabu is Mandatory?</h2>
            <p>An unregistered agreement binds only its original signatories. To give it full property standing that binds future buyers or heirs, **the co-ownership agreement must be registered in the Land Registry (Tabu)**.</p>
        """
    },
    {
        'slug': 'partition-real-estate-joint-ownership',
        'practiceAreaId': 'partnerships-coownership',
        'image': 'article_partnership_2.png',
        'date': '20.03.2026',
        'readTime': '5 min read',
        'categoryHe': 'הסכמי שיתוף',
        'categoryEn': 'Partnerships & Co-ownership',
        'titleHe': 'פירוק שיתוף במקרקעין: זכותו של כל שותף — והדרך הנכונה לממש אותה',
        'titleEn': 'Partition of Joint Real Estate: Every Owners Right & How to Exercise It',
        'descHe': 'מסלולי הפירוק (חלוקה בעין, מכירה, התמחרות), שיקולי בית המשפט, ואסטרטגיה נכונה לכל צד.',
        'descEn': 'Partition pathways (physical division, sale, auction), court considerations, and strategic steps for each party.',
        'contentHe': """
            <p>כאשר שותפים במקרקעין אינם מצליחים להגיע להסכמות לגבי ניהול הנכס, או כאשר אחד השותפים מעוניין לממש את השקעתו ולצאת מהשותפות בעוד האחרים מסרבים למכור, המוצא המשפטי האחרון הוא תביעה לפירוק שיתוף. החוק הישראלי מעניק לכל שותף זכות יסוד לדרוש את פירוק השיתוף בכל עת.</p>
            
            <h2>הזכות לתבוע פירוק שיתוף: זכות יסוד כמעט מוחלטת</h2>
            <p>סעיף 37 לחוק המקרקעין קובע באופן ברור: **כל שותף במקרקעין משותפים זכאי בכל עת לדרוש פירוק השיתוף**. בתי המשפט בישראל רואים בשותפות מקרקעין ללא הסכמה מצב לא רצוי המונע את פיתוח הקרקע, ולכן כמעט תמיד יענו לבקשת הפירוק, למעט במקרים חריגים של חוסר תום לב קיצוני.</p>
            
            <h2>שלושת מסלולי הפירוק על פי החוק</h2>
            <p>בית המשפט יבחן את הדרך הנכונה לפירוק השיתוף על פי סדר עדיפויות מוגדר בחוק:
            1. **חלוקה בעין**: אם הקרקע ניתנת לחלוקה פיזית (למשל, מגרש שניתן לחלקו לשני מגרשים עצמאיים לפי תוכניות מתאר בתוקף), בית המשפט יעדיף דרך זו.
            2. **רישום בית משותף**: במידה ומדובר בבניין מגורים, הפירוק יבוצע על ידי רישום המבנה כבית משותף והקצאת הדירות לשותפים השונים בהתאם לחלקם.
            3. **מכירה וחלוקת הפדיון**: אם הנכס אינו ניתן לחלוקה בעין (כמו דירת מגורים בודדת), בית המשפט יורה על מכירת הנכס כולו בדרך של מכירה פומבית (הוצאה לפועל) או באמצעות כונס נכסים, וחלוקת הכסף בין השותפים לפי חלקם היחסי בטאבו.</p>
            
            <h2>אסטרטגיה וליווי משפטי</h2>
            <p>ניהול תביעת פירוק שיתוף דורש תכנון אסטרטגי קפדני. מכירה באמצעות כונס נכסים עלולה להוביל למכירת הנכס במחיר נמוך ממחיר השוק בשל עלויות הכינוס (שכר טרחת כונס, פרסום). לכן, עורך דין מנוסה ינסה להוביל את השותפים להליך התמחרות פנימי או מכירה מוסכמת בשוק החופשי, כדי למקסם את הרווח לכל הצדדים ולמנוע הוצאות מיותרות.</p>
        """,
        'contentEn': """
            <p>When co-owners cannot agree on property management, or when one wishes to liquidate their holdings but others refuse to sell, a Partition Suit is the ultimate legal remedy under Israeli law.</p>
            
            <h2>The Right to Demand Partition: An Absolute Principle</h2>
            <p>Section 37 of the Land Law states: **any co-owner is entitled to demand partition at any time**. Israeli courts favor partition since forced co-ownership often blocks property development.</p>
            
            <h2>Three Statutory Partition Pathways</h2>
            <p>Courts evaluate partition options in a defined legal hierarchy:
            1. **Physical Partition (Chaluka B\'Ain)**: Preferred if the land can be subdivided according to zoning laws.
            2. **Condominium Registration**: Registering a residential building as a condominium and assigning units to owners.
            3. **Sale and Proceeds Distribution**: If the property is indivisible (like a single apartment), the court orders a public sale (usually via receivership) and divides the proceeds.</p>
            
            <h2>Strategy and Legal Representation</h2>
            <p>Receivership sales can result in lower prices due to court fees. An experienced attorney will guide partners toward an internal auction or agreed-upon market sale to maximize returns and avoid fees.</p>
        """
    },
    {
        'slug': 'inherited-real-estate-disputes',
        'practiceAreaId': 'partnerships-coownership',
        'image': 'article_partnership_3.png',
        'date': '15.03.2026',
        'readTime': '5 min read',
        'categoryHe': 'הסכמי שיתוף',
        'categoryEn': 'Partnerships & Co-ownership',
        'titleHe': 'נדל"ן בירושה: כשכמה יורשים מחזיקים בנכס אחד',
        'titleEn': 'Inherited Real Estate: Managing Co-ownership Among Heirs',
        'descHe': 'מה עושים כשיורש אחד גר בנכס, אחר רוצה למכור ושלישי שותק — דמי שימוש ראויים, הסכמי חלוקה ופתרונות מעשיים.',
        'descEn': 'What to do when one heir lives in the property, another wants to sell, and a third remains silent - usage fees and solutions.',
        'contentHe': """
            <p>קבלת דירת מגורים או מגרש בירושה היא לרוב בשורה משמחת, אך כאשר הנכס מועבר למספר יורשים במשותף (למשל, אחים הרשומים בטאבו בחלקים שווים), השמחה עלולה להתחלף מהר מאוד בסכסוכים קשים לגבי עתיד הנכס.</p>
            
            <h2>התרחיש הנפוץ: יורש המשתמש בנכס ללא הסכמת השאר</h2>
            <p>אחת המחלוקות השכיחות ביותר מתרחשת כאשר אחד היורשים גר בפועל בדירה של ההורים שנפטרו, בעוד שאר האחים מעוניינים להשכירה לשוכר חיצוני או למכור אותה ולחלק את הכסף. על פי החוק, שותף רשאי להשתמש בנכס המשותף שימוש סביר ללא הסכמת השאר, אך עליו לאפשר גם לשאר השותפים להשתמש בו. במידה והוא מונע זאת מהם, עליהם לדרוש "דמי שימוש ראויים" (שכר דירה יחסי לפי חלקם בנכס).</p>
            
            <h2>הפתרון המועדף: הסכם חלוקת עיזבון טרם הרישום בטאבו</h2>
            <p>כדי למנוע שותפות כפויה בנכס יחיד, הכלי המשפטי המומלץ ביותר הוא חתימה על **הסכם חלוקת עיזבון** בין היורשים עוד לפני רישום צו הירושה בטאבו. הסכם זה מאפשר לבצע "איזון משאבים" פנימי: למשל, יורש אחד יקבל את הבעלות המלאה על הדירה, בעוד היורשים האחרים יקבלו כספי נזילות מהעיזבון או נכסים אחרים. חלוקה זו פותרת את בעיית השותפות ואינה נחשבת לעסקת מקרקעין חדשה לעניין מיסוי.</p>
            
            <h2>תביעה לפירוק שיתוף כמוצא אחרון</h2>
            <p>אם היורשים אינם מגיעים להסכמות, המוצא האחרון הוא פנייה לבית המשפט לענייני משפחה בתביעה לפירוק שיתוף מקרקעין. בית המשפט יורה בדרך כלל על מכירת הדירה בשוק החופשי באמצעות כונס נכסים וחלוקת הכספים. מדובר בהליך יקר וממושך שממומן מכספי העיזבון, ולכן עדיף להגיע להסכמות מחוץ לכותלי בית המשפט בליווי עורך דין מנוסה.</p>
        """,
        'contentEn': """
            <p>Inheriting a property with siblings is a great asset, but registered co-ownership among multiple heirs can quickly spiral into legal disputes over property management.</p>
            
            <h2>Common Dispute: One Heir Occupying the Property</h2>
            <p>A classic dispute arises when one heir lives in the deceased parents\' apartment, while others want to rent it out or sell it. The occupying heir must pay "reasonable usage fees" (rent) to the other heirs.</p>
            
            <h2>The Preferred Solution: Estate Distribution Agreements</h2>
            <p>To avoid forced co-ownership, heirs should sign an **Estate Distribution Agreement** before registering the inheritance in the Tabu. One heir can receive full ownership of the home, while others take cash assets.</p>
            
            <h2>Partition Suits as a Last Resort</h2>
            <p>If heirs remain in conflict, the last resort is a partition lawsuit in Family Court. The court will order the sale of the home and divide the proceeds, which is costly and should be avoided by negotiating early.</p>
        """
    },
    # --- Category 7: Wills & Inheritance ---
    {
        'slug': 'mutual-wills-spouses',
        'practiceAreaId': 'wills-inheritance',
        'image': 'article_wills_1.png',
        'date': '28.02.2026',
        'readTime': '5 min read',
        'categoryHe': 'צוואות וירושות',
        'categoryEn': 'Wills & Inheritance',
        'titleHe': 'צוואה הדדית בין בני זוג: יתרונות, מגבלות והמלכודות שחשוב להכיר',
        'titleEn': 'Mutual Wills Between Spouses: Benefits, Limitations, and Pitfalls',
        'descHe': 'מתי צוואה הדדית היא הפתרון הנכון, ומה קורה כשבן הזוג שנותר בחיים רוצה לשנות אותה.',
        'descEn': 'When a mutual will is the right choice, and what happens when the surviving spouse wishes to modify their wishes.',
        'contentHe': """
            <p>צוואה הדדית היא כלי משפטי ייחודי ומבוקש מאוד בקרב בני זוג בישראל. היא מאפשרת לבני הזוג לערוך צוואות המסתמכות זו על זו, מתוך רצון להבטיח את עתידו של בן הזוג הנותר בחיים, ולאחר מכן להסדיר את חלוקת הרכוש לילדים המשותפים.</p>
            
            <h2>מהי צוואה הדדית?</h2>
            <p>חוק הירושה הישראלי מאפשר לבני זוג לערוך צוואות מתוך הסתמכות הדדית. לרוב, הנוסח המקובל בצוואה הדדית קובע כי במקרה של פטירת אחד מבני הזוג, רכושו יעבור במלואו לבן הזוג הנותר בחיים. רק לאחר פטירת שני בני הזוג, יעבור הרכוש שנותר לילדיהם המשותפים (או למוטבים אחרים שנקבעו מראש).</p>
            
            <h2>הגנת בן הזוג השורד מפני תביעות ילדים</h2>
            <p>היתרון המרכזי של צוואה הדדית הוא מניעת מצבים קשים שבהם, לאחר פטירת אחד ההורים, הילדים דורשים לקבל את חלקם בירושה על פי דין (חצי מהרכוש), מה שעלול להכריח את ההורה שנותר בחיים למכור את דירת המגורים כדי לשלם לילדים. הצוואה ההדדית מבטיחה להורה השורד שקט נפשי ובעלות מלאה על הרכוש כל עוד הוא בחיים.</p>
            
            <h2>מגבלות חוקיות על ביטול או שינוי הצוואה</h2>
            <p>הסתמכות הדדית יוצרת קושי משפטי: מה קורה אם בן הזוג השורד מחליט לשנות את דעתו ומוריש את הרכוש לצד שלישי? החוק קובע הגבלות נוקשות על ביטול צוואה הדדית:
            * **בחיי שני בני הזוג**: בן זוג המבקש לבטל את צוואתו חייב למסור הודעה בכתב לבן הזוג השני, מה שמבטל אוטומטית גם את הצוואה של השני.
            * **לאחר פטירת אחד מבני הזוג**: בן הזוג הנותר בחיים המבקש לשנות את צוואתו חייב לוותר על כל חלק בעיזבון שקיבל מבן הזוג שנפטר, או להשיב את הרכוש בפועל לעיזבון לטובת המוטבים המקוריים.</p>
        """,
        'contentEn': """
            <p>A Mutual Will is a unique and popular legal tool for spouses in Israel. It allows couples to draft wills that rely on each other, ensuring the financial security of the surviving spouse before inheritance passes to the children.</p>
            
            <h2>What is a Mutual Will?</h2>
            <p>The Inheritance Law allows spouses to make joint wills. Typically, they state that upon the death of one spouse, their entire estate passes to the survivor. Only after both pass does the remaining estate go to their children.</p>
            
            <h2>Protecting the Surviving Spouse from Claims</h2>
            <p>The primary benefit is preventing situations where children demand their statutory share immediately upon one parent\'s death, forcing the surviving parent to sell their home to pay the children.</p>
            
            <h2>Legal Restrictions on Revoking or Amending</h2>
            <p>Mutual wills carry strict rules for revocation:
            * **While both are alive**: One must give written notice to the other, which automatically voids both wills.
            * **After one dies**: The survivor must renounce any inherited share from the deceased spouse to amend the will.</p>
        """
    },
    {
        'slug': 'inheritance-vs-probate-order',
        'practiceAreaId': 'wills-inheritance',
        'image': 'article_wills_2.png',
        'date': '20.02.2026',
        'readTime': '4 min read',
        'categoryHe': 'צוואות וירושות',
        'categoryEn': 'Wills & Inheritance',
        'titleHe': 'צו ירושה או צו קיום צוואה — מה ההבדל, ואיך מגישים בקשה נכון',
        'titleEn': 'Inheritance Order vs. Probate Order: Key Differences and Filing Guide',
        'descHe': 'ההליך מול הרשם לענייני ירושה, מסמכים נדרשים, התנגדויות, ומתי ההליך מסתבך.',
        'descEn': 'The process before the Registrar of Inheritance Affairs, required documents, objections, and handling complexities.',
        'contentHe': """
            <p>לאחר פטירתו של אדם, רכושו ונכסיו אינם עוברים אוטומטית ליורשיו. על מנת לקבל סמכות חוקית לנהל את נכסי העיזבון, למשוך כספים מחשבונות בנק או לרשום דירת מגורים על שם היורשים בטאבו, יש לפנות לרשם לענייני ירושה לקבלת צו רשמי.</p>
            
            <h2>1. צו ירושה (Inheritance Order)</h2>
            <p>צו ירושה מוגש במקרים שבהם הנפטר **לא השאיר אחריו צוואה בכתב**. במצב זה, חלוקת הרכוש מבוצעת על פי הוראות חוק הירושה בישראל (ירושה על פי דין). על פי החוק, קרובי המשפחה מדרגה ראשונה (בן זוג וילדים) הם היורשים העיקריים — בן הזוג מקבל מחצית מהרכוש והילדים מקבלים את החצי השני בחלקים שווים ביניהם.</p>
            
            <h2>2. צו קיום צוואה (Probate Order)</h2>
            <p>צו קיום צוואה מוגש במקרים שבהם הנפטר **הותיר אחריו צוואה תקפה**. הצו מעניק לצוואה תוקף משפטי של פסק דין ומורה לרשום את הזכויות בנכסים על פי ההוראות הספציפיות שקבע הנפטר בצוואתו, ללא קשר לכללי הירושה על פי דין.</p>
            
            <h2>כיצד מגישים את הבקשה לרשם לענייני ירושה?</h2>
            <p>כיום ניתן להגיש את הבקשות באופן מקוון באתר הרשם לענייני ירושה. יש לצרף מסמכים חיוניים: תעודת פטירה מקורית, אישור על משלוח הודעה בדואר רשום לכל היורשים הנוספים, ואת הצוואה המקורית (במקרה של צו קיום צוואה). לאחר ההגשה, מפרסם הרשם הודעה בעיתונות היומית כדי לאפשר הגשת התנגדויות לצו בתוך 14 ימים.</p>
        """,
        'contentEn': """
            <p>After a person passes away, their assets do not transfer automatically. To register inherited property, clear bank accounts, or manage the estate, you must obtain a formal order from the Registrar of Inheritance.</p>
            
            <h2>1. Succession/Inheritance Order (Tzav Yerusha)</h2>
            <p>An inheritance order is filed when the deceased **did not leave a will**. In this case, assets are distributed according to default statutory rules, typically split 50/50 between the spouse and children.</p>
            
            <h2>2. Probate Order (Tzav Kiyum Tzava\'a)</h2>
            <p>A probate order is requested when the deceased **left a valid will**. The order validates the will, directing executors to distribute all property strictly according to the deceased\'s specific instructions.</p>
            
            <h2>Filing the Application</h2>
            <p>Applications can be filed online with the Registrar. Documents needed include a death certificate, proof of notice to other heirs, and the original will. The registrar publishes a public notice to allow objections within 14 days.</p>
        """
    },
    {
        'slug': 'estate-distribution-agreement',
        'practiceAreaId': 'wills-inheritance',
        'image': 'article_wills_3.png',
        'date': '10.02.2026',
        'readTime': '5 min read',
        'categoryHe': 'צוואות וירושות',
        'categoryEn': 'Wills & Inheritance',
        'titleHe': 'הסכם חלוקת עיזבון בין יורשים: הכלי שחוסך מס ומונע מלחמות משפחתיות',
        'titleEn': 'Estate Distribution Agreements: Reducing Taxes and Family Conflict',
        'descHe': 'איך חלוקה מוסכמת ונכונה של נכסי העיזבון יכולה לחסוך מס שבח ומס רכישה — ובאילו תנאים.',
        'descEn': 'How a negotiated distribution of inherited assets can save capital gains and purchase taxes, and the rules to follow.',
        'contentHe': """
            <p>בעת חלוקת עיזבון הכולל מספר נכסי נדל"ן בין מספר יורשים, רישום אוטומטי של הנכסים בטאבו על שם כולם במשותף עלול ליצור בעיות רבות. הסכם חלוקת עיזבון הוא כלי משפטי ותכנוני רב עוצמה המאפשר ליורשים לחלק את נכסי העיזבון ביניהם באופן מותאם אישית, תוך ניצול הטבות מס משמעותיות.</p>
            
            <h2>מהו הסכם חלוקת עיזבון?</h2>
            <p>הסכם חלוקת עיזבון הוא חוזה הנחתם בין כלל היורשים המוסכמים של הנפטר. במסגרת ההסכם, רשאים היורשים לסטות מהחלוקה המקורית שנקבעה בצוואה או בחוק הירושה, ולבצע "איזון" של הנכסים. לדוגמה, אם העיזבון כולל שתי דירות מגורים ושני יורשים, הם יכולים להסכים כי כל יורש יקבל דירה אחת בבעלות מלאה, במקום ששני היורשים יהיו שותפים בחצי מכל דירה.</p>
            
            <h2>יתרון המס העצום: פטור ממס שבח ומס רכישה</h2>
            <p>על פי סעיף 5(ג)(4) לחוק מיסוי מקרקעין, חלוקת נכסי עיזבון בין יורשים אינה נחשבת כ"עסקה במקרקעין", ועל כן היא **פטורה לחלוטין ממס שבח ומס רכישה**. פטור זה חל בתנאי מפתח אחד: החלוקה מבוצעת אך ורק מתוך נכסי העיזבון עצמם (ללא הוספת כספים חיצוניים של היורשים לצורך ביצוע האיזון).</p>
            
            <h2>כיצד מנסחים את ההסכם נכון?</h2>
            <p>ניסוח ההסכם דורש ליווי מקצועי של עורך דין מקרקעין המתמחה בדיני ירושה ומיסוי. חובה לערוך את ההסכם **לפני** רישום צו הירושה בטאבו ולפני שבוצעו פעולות חלוקה ראשוניות בנכסים, ולהציג שמאות מקרקעין מדויקת המגבה את שווי הנכסים ומבטיחה הגנה מלאה על היורשים מול רשויות המס.</p>
        """,
        'contentEn': """
            <p>When dividing an estate with multiple properties among heirs, registering them jointly in the Tabu causes future issues. An Estate Distribution Agreement lets heirs divide assets tailored to their needs while enjoying tax benefits.</p>
            
            <h2>What is an Estate Distribution Agreement?</h2>
            <p>This is a contract signed by all heirs. They can deviate from the default statutory partition, swapping assets. For example, if there are two homes and two heirs, each can take full title to one home instead of joint ownership.</p>
            
            <h2>The Major Tax Benefit: Exemption from Real Estate Taxes</h2>
            <p>Under Section 5(c)(4) of the Property Tax Law, estate distribution among heirs is not considered a taxable transaction and is **exempt from Mas Shevach and Mas Rechisha**, provided only estate assets are used.</p>
            
            <h2>Drafting the Agreement Correctly</h2>
            <p>The agreement must be drafted **before** registering the inheritance in the Tabu. Hiring a real estate and probate lawyer ensures your filings satisfy tax authorities.</p>
        """
    },
    # --- Category 8: Ongoing POA ---
    {
        'slug': 'ongoing-poa-importance-over-50',
        'practiceAreaId': 'ongoing-power-of-attorney',
        'image': 'article_poa_1.png',
        'date': '05.02.2026',
        'readTime': '4 min read',
        'categoryHe': 'ייפוי כוח מתמשך',
        'categoryEn': 'Ongoing POA',
        'titleHe': 'ייפוי כוח מתמשך — למה כל אדם מעל גיל 50 צריך לשקול אותו עכשיו',
        'titleEn': 'Ongoing Power of Attorney: Why Everyone Over 50 Should Secure One Now',
        'descHe': 'ההבדל בין ייפוי כוח מתמשך לאפוטרופסות, ולמה עדיף להחליט בעצמכם מי יחליט עבורכם.',
        'descEn': 'The differences between ongoing POA and guardianship, and why you should decide who manages your affairs.',
        'contentHe': """
            <p>החיים מזמנים לנו מצבים בלתי צפויים שבהם אנו עלולים לאבד את היכולת לקבל החלטות באופן עצמאי — בשל תאונה, מחלה קשה או תהליכי זיקנה (דמנציה). בעבר, הפתרון היחיד במצבים אלו היה מינוי אפוטרופוס על ידי בית משפט. כיום, קיים כלי מהפכני, מכבד ומתקדם בהרבה: ייפוי כוח מתמשך.</p>
            
            <h2>ייפוי כוח מתמשך מול אפוטרופסות: הבדל של שמים וארץ</h2>
            <p>ההבדל המרכזי בין שני הכלים הללו נעוץ בשליטה ובחופש הבחירה שלכם:
            * **אפוטרופסות**: הליך משפטי המתקיים רק **לאחר** שכבר איבדתם את הכשירות. בית המשפט הוא שמחליט מי ינהל את חייכם (לעיתים גורם זר או עמותה), ומיופה הכוח נדרש להגיש דוחות כספיים מתישים לאפוטרופוס הכללי ומחויב לקבל אישור בית משפט לכל פעולה מהותית (כמו מכירת דירה).
            * **ייפוי כוח מתמשך**: מסמך תכנוני שאתם עורכים בעודכם **בריאים וכשירים לחלוטין**. אתם מחליטים בעצמכם מי יטפל בכם, אילו סמכויות ינתנו לו, ואף יכולים להשאיר הנחיות מפורטות לגבי רצונכם (למשל, היכן תרצו לגור ואיזה טיפול רפואי לקבל).</p>
            
            <h2>הגנה על עצמאותכם ורצונכם החופשי</h2>
            <p>ייפוי כוח מתמשך מונע מאבקים משפחתיים קשים ומאפשר לכם לשמור על כבודכם העצמי. הוא מעניק למיופי הכוח שבחרתם (בדרך כלל בני זוג או ילדים) את הסמכות לפעול מיידית לטובתכם ללא צורך בפנייה לבתי משפט, מה שחוסך זמן יקר ובירוקרטיה מתישה ברגעים הקשים ביותר.</p>
        """,
        'contentEn': """
            <p>Life can present unexpected situations where we lose our decision-making capacity due to accidents or cognitive decline. In the past, the only solution was court-appointed guardianship. Today, we have the Ongoing POA.</p>
            
            <h2>Ongoing POA vs. Guardianship: A World of Difference</h2>
            <p>The core difference lies in control and choice:
            * **Guardianship**: A reactive court process initiated *after* capacity is lost. The court appoints a guardian (sometimes a corporate body) who must file tedious financial audits and seek court approvals.
            * **Ongoing POA**: A proactive document drafted while you are **fully healthy and competent**. You decide who manages your life, what powers they hold, and outline detailed instructions.</p>
            
            <h2>Protecting Your Independence and Wishes</h2>
            <p>An ongoing POA prevents family conflict and protects your dignity, granting trusted representatives (spouse/children) immediate power to act on your behalf without court approvals, saving crucial time.</p>
        """
    },
    {
        'slug': 'three-areas-ongoing-poa',
        'practiceAreaId': 'ongoing-power-of-attorney',
        'image': 'article_poa_2.png',
        'date': '01.02.2026',
        'readTime': '4 min read',
        'categoryHe': 'ייפוי כוח מתמשך',
        'categoryEn': 'Ongoing POA',
        'titleHe': 'רכוש, רפואה ועניינים אישיים: שלושת התחומים בייפוי כוח מתמשך ואיך מתאימים אותם אישית',
        'titleEn': 'Property, Medical, and Personal Affairs: The Three Pillars of Ongoing POA',
        'descHe': 'הנחיות מקדימות, מינוי מיודעים, וההחלטות שכדאי לחשוב עליהן לפני הפגישה אצל עורך הדין.',
        'descEn': 'Preliminary directives, choosing informed persons, and key decisions to consider before your legal consultation.',
        'contentHe': """
            <p>עריכת ייפוי כוח מתמשך אינה פעולה טכנית אלא תהליך אישי של תכנון העתיד. החוק מאפשר לכם להעניק סמכויות למיופי הכוח בשלושה תחומי חיים מרכזיים, ולקבוע הנחיות מפורטות ומותאמות אישית לכל אחד מהם.</p>
            
            <h2>1. העניינים הרכושיים (Financial Affairs)</h2>
            <p>תחום זה מסדיר את ניהול כלל הנכסים והכספים שלכם. במסגרתו, אתם מעניקים למיופה הכוח סמכות לנהל חשבונות בנק, לשלם חשבונות שוטפים, לנהל תיקי השקעות, לגבות כספי פנסיה וקצבאות, ולנהל נכסי נדל"ן שבבעלותכם (כולל השכרתם). ניתן להגביל את מיופה הכוח מראש, למשל לקבוע כי הוא אינו מוסמך למכור את דירת המגורים שלכם או לתת מתנות מעל סכום מסוים.</p>
            
            <h2>2. העניינים האישיים (Personal Affairs)</h2>
            <p>תחום זה נוגע לרווחתכם האישית, לאיכות חייכם ולצרכים היומיומיים שלכם. הוא כולל החלטות לגבי מקום המגורים שלכם (המשך מגורים בבית עם מטפל צמוד או מעבר לבית אבות ספציפי), דאגה לצרכי תזונה, לבוש, תרבות ופנאי, וכן טיפול בעניינים סיעודיים ושיקומיים שוטפים.</p>
            
            <h2>3. העניינים הרפואיים (Medical Affairs)</h2>
            <p>תחום זה מקנה למיופה הכוח סמכות לקבל החלטות רפואיות בשמכם, לחתום על הסכמות לטיפולים או ניתוחים, ולבחור את הגורמים הרפואיים המטפלים. ניתן להשאיר הנחיות מקדימות ברורות לגבי סוגי טיפולים מועדפים, ואף להתייחס לנושאים רגישים של טיפולים מאריכי חיים במצבים סופניים.</p>
        """,
        'contentEn': """
            <p>Drafting an ongoing POA is a highly personal future-planning process. The law allows you to delegate authority across three core life pillars, complete with detailed instructions.</p>
            
            <h2>1. Financial/Property Pillar</h2>
            <p>Regulates the management of your assets. It empowers your representative to manage bank accounts, investments, collect pension funds, and lease real estate, with optional limits like prohibiting home sales.</p>
            
            <h2>2. Personal Affairs Pillar</h2>
            <p>Concerns your day-to-day well-being and lifestyle. It covers housing choices (staying home with a caregiver or moving to a specific care home), nutritional needs, hobbies, and social care.</p>
            
            <h2>3. Medical Affairs Pillar</h2>
            <p>Grants authority to make healthcare decisions, sign consents for surgeries, and select treatment options, including outlining specific directives for end-of-life care.</p>
        """
    },
    {
        'slug': 'activation-and-supervision-ongoing-poa',
        'practiceAreaId': 'ongoing-power-of-attorney',
        'image': 'article_poa_3.png',
        'date': '15.01.2026',
        'readTime': '4 min read',
        'categoryHe': 'ייפוי כוח מתמשך',
        'categoryEn': 'Ongoing POA',
        'titleHe': 'מתי ייפוי כוח מתמשך נכנס לתוקף — ומי מפקח על מיופה הכוח?',
        'titleEn': 'Ongoing POA Activation and Supervision: Protecting Your Interests',
        'descHe': 'מנגנון הכניסה לתוקף, תפקיד האפוטרופוס הכללי, וההגנות המובנות מפני ניצול לרעה.',
        'descEn': 'The activation process, the role of the Administrator General, and built-in protections against financial abuse.',
        'contentHe': """
            <p>אחד החששות הגדולים ביותר של אנשים השוקלים לערוך ייפוי כוח מתמשך הוא שמא מיופה הכוח ינצל לרעה את כוחו ויפעל בנכסיהם בעודם כשירים. חוק הירושה והאפוטרופסות כולל מנגנוני הגנה קפדניים וברורים כדי למנוע מצבים אלו ולהבטיח פיקוח מלא.</p>
            
            <h2>מנגנון הכניסה לתוקף: רק כשאינכם מסוגלים להבין בדבר</h2>
            <p>הערה קריטית: **ייפוי הכוח אינו מקנה למיופה הכוח שום סמכות כל עוד אתם כשירים ובריאים**. כניסת ייפוי הכוח לתוקף מתבצעת רק כאשר נקבע כי הממנה אינו מסוגל עוד להבין בדבר שלשמו ניתן ייפוי הכוח. הממנה יכול לקבוע מראש מהו המדד לכך (למשל, חוות דעת של רופא מומחה ספציפי או בדיקה רפואית מסוימת). בהיעדר קביעה כזו, החוק דורש חוות דעת רפואית מוסמכת הקובעת את אובדן הכשירות.</p>
            
            <h2>תהליך ההפעלה מול האפוטרופוס הכללי</h2>
            <p>כדי להפעיל את ייפוי הכוח, על מיופה הכוח להגיש הצהרת כניסה לתוקף לאפוטרופוס הכללי במשרד המשפטים, בצירוף חוות הדעת הרפואית הנדרשת. רק לאחר שהאפוטרופוס הכללי בודק את המסמכים ומנפיק "אישור על כניסה לתוקף", מקבל מיופה הכוח את הסמכות לפעול מול הבנקים, רשויות המס והמוסדות השונים.</p>
            
            <h2>מנגנוני פיקוח והגנה: מינוי "מיודעים"</h2>
            <p>על מנת למנוע בדידות תפקודית וחשש מניצול, הממנה יכול להגדיר בייפוי הכוח "אדם מיודע" (למשל, חבר קרוב או בן משפחה נוסף שאינו מיופה כוח). מיופה הכוח מחויב על פי חוק לדווח למיודע על פעולות מהותיות שביצע ולשתף אותו בהחלטות. במידה ומתעורר חשד לניצול לרעה, רשאי כל אדם לפנות לאפוטרופוס הכללי או לבית המשפט בדרישה לבטל את ייפוי הכוח.</p>
        """,
        'contentEn': """
            <p>A primary concern when setting up an ongoing POA is the fear of abuse of power. The law includes strict safeguards and supervision protocols to protect your interests.</p>
            
            <h2>Activation Protocol: Only Upon Confirmed Loss of Capacity</h2>
            <p>Note: **the POA grants no authority while you are fully competent**. The activation requires proof that you can no longer manage your affairs, usually evidenced by a professional medical opinion.</p>
            
            <h2>Filing with the Administrator General</h2>
            <p>To activate the POA, the representative must submit an activation declaration and medical certificate to the Administrator General. Only upon receiving the official authorization can they act.</p>
            
            <h2>Supervision Measures: "Informed Persons" (Meyuda\'im)</h2>
            <p>You can designate "informed persons" (friends/relatives) who must be updated on decisions by the representative, ensuring transparency and preventing isolated financial abuse.</p>
        """
    },
    # --- Category 9: Corporate & Non-Profit ---
    {
        'slug': 'founders-agreement-startup-importance',
        'practiceAreaId': 'corporate-non-profit-registration',
        'image': 'article_company_1.png',
        'date': '10.01.2026',
        'readTime': '5 min read',
        'categoryHe': 'רישום חברות ועמותות',
        'categoryEn': 'Corporate & Non-Profit',
        'titleHe': 'הסכם מייסדים: המסמך שיקבע אם החברה שלכם תשרוד את הריב הראשון',
        'titleEn': 'Founders Agreements: Safeguarding Your Startup Before the First Conflict',
        'descHe': 'חלוקת מניות, מנגנוני הכרעה במבוי סתום, Vesting וזכויות סירוב — מה שחייבים לסגור לפני שמתחילים.',
        'descEn': 'Equity distribution, deadlock resolution, reverse vesting, and right of first refusal - terms you must define before launching.',
        'contentHe': """
            <p>הקמת סטארט-אפ או עסק חדש עם שותפים מלווה בהתרגשות רבה ובאנרגיות גבוהות. בשלבים הראשוניים, השותפים נוטים להסכים על הכול בעל פה ולהאמין כי יחסיהם הטובים ישרדו כל קושי. אולם, המציאות העסקית מוכיחה כי היעדר הסכם מייסדים כתוב ומקצועי הוא אחד הגורמים המרכזיים לקריסת מיזמים צעירים.</p>
            
            <h2>1. חלוקת מניות והגדרת תפקידים</h2>
            <p>הסכם המייסדים מסדיר תחילה את חלוקת אחוזי הבעלות (המניות) בחברה בין השותפים, ומגדיר את התפקידים, תחומי האחריות והיקף המשרה של כל מייסד. חשוב לקבוע מנגנון של **Vesting** (הבשלה הדרגתית של מניות) — מנגנון המבטיח כי שותף שעוזב את החברה בשלב מוקדם לא יישאר עם חלק גדול מהמניות מבלי שתרם את חלקו לחברה לאורך זמן.</p>
            
            <h2>2. מנגנוני קבלת החלטות ופתרון מבוי סתום (Deadlock)</h2>
            <p>כאשר שותפים מחזיקים בחלקים שווים (50/50), נוצר סיכון מובנה למצבי "תיקו" שבהם לא ניתן לקבל החלטות קריטיות (כמו גיוס עובדים, רכישת ציוד או הכנסת משקיע). הסכם המייסדים חייב להגדיר מנגנונים לפתרון מבוי סתום: הכרעה על ידי בורר חיצוני מוסכם, מנגנון במבו (BMBY - Buy Me Buy You) המאפשר לשותף אחד לרכוש את חלקו של השני, או זכות הכרעה לדירקטור חיצוני.</p>
            
            <h2>3. הגבלות על העברת מניות וזכויות הגנה</h2>
            <p>כדי להגן על החברה מפני כניסת גורמים עוינים או לא מוכרים, ההסכם מעגן הגבלות על מכירת מניות לצד שלישי:
            * **זכות סירוב ראשונה (ROFR)**: חובה להציע את המניות תחילה לשותפים הקיימים באותם תנאים.
            * **זכות הצטרפות (Tag-Along)**: זכות לשותפי המיעוט להצטרף לעסקת מכירה של שותף הרוב באותם תנאים.</p>
        """,
        'contentEn': """
            <p>Launching a startup with partners is an exciting phase. However, research shows that the absence of a written Founders\' Agreement is one of the main reasons young ventures collapse.</p>
            
            <h2>1. Share Allocation and Roles</h2>
            <p>The founders\' agreement regulates ownership shares and clarifies roles. Setting a **Vesting** schedule ensures that a partner departing early does not retain equity they did not earn.</p>
            
            <h2>2. Decision-Making and Deadlock Resolution</h2>
            <p>Equal split partnerships (50/50) run the risk of deadlocks. The agreement must establish resolution models, such as BMBY (Buy Me Buy You) clauses, arbitration, or independent tie-breaking votes.</p>
            
            <h2>3. Share Transfer Restrictions</h2>
            <p>To prevent third-party interference, the agreement details transfer restrictions: Right of First Refusal (ROFR) and Tag-Along rights protecting minority shareholders during buyouts.</p>
        """
    },
    {
        'slug': 'sole-proprietorship-vs-corporation',
        'practiceAreaId': 'corporate-non-profit-registration',
        'image': 'article_company_2.png',
        'date': '05.01.2026',
        'readTime': '4 min read',
        'categoryHe': 'רישום חברות ועמותות',
        'categoryEn': 'Corporate & Non-Profit',
        'titleHe': 'עוסק מורשה או חברה בע"מ? המדריך המשפטי להחלטה הראשונה של כל עסק',
        'titleEn': 'Sole Proprietorship vs. LTD Company: The Legal Guide to Choosing Your Business Entity',
        'descHe': 'שיקולי אחריות אישית, מיסוי ותדמית — ומתי השלב הנכון להתאגד כחברה.',
        'descEn': 'Liability considerations, corporate taxation, and branding - and when is the right time to incorporate.',
        'contentHe': """
            <p>כל יזם המקים עסק חדש בישראל עומד בפני החלטה מבנית גורלית: האם להירשם כעוסק מורשה (או עוסק פטור) או להתאגד כחברה בעירבון מוגבל (חברה בע"מ) ברשם החברות. להחלטה זו השלכות משפטיות ומיסויות דרמטיות על עתיד העסק ועל רכושו האישי של היזם.</p>
            
            <h2>1. שאלת האחריות המשפטית (מסך ההתאגדות)</h2>
            <p>זהו ההבדל המשפטי המשמעותי ביותר:
            * **עוסק מורשה**: אין הפרדה משפטית בין העסק לבין האדם הפרטי. אם העסק נקלע לחובות או נתבע על ידי לקוחות, נושי העסק יכולים לרדת לנכסיו האישיים של היזם (דירת מגורים, רכב, חסכונות משפחתיים).
            * **חברה בע"מ**: חברה היא אישיות משפטית נפרדת מבעליה. "מסך ההתאגדות" מגן על בעלי המניות, כך שחובות החברה שייכים לחברה בלבד ולא ניתן לרדת לנכסיהם האישיים של הבעלים (למעט במקרים חריגים של הונאה המצדיקים "הרמת מסך").</p>
            
            <h2>2. היבטי מיסוי ותדמית עסקית</h2>
            <p>חברות בע"מ נהנות משיעור מס קבוע (מס חברות העומד על 23% נכון לשנת 2026), בעוד שעוסק מורשה ממוסה לפי מדרגות מס הכנסה אישיות של עד 50%. בנוסף, התאגדות כחברה בע"מ משדרת רצינות ותדמית של עסק מבוסס מול בנקים, ספקים ולקוחות גדולים בישראל ובחו"ל, ומאפשרת הכנסת משקיעים באמצעות הקצאת מניות.</p>
            
            <h2>מתי זה הזמן הנכון לעבור לחברה בע"מ?</h2>
            <p>ככלל אצבע פיננסי ומשפטי, מומלץ לעבור לעבודה כחברה בע"מ כאשר מחזור הפעילות של העסק גדל והרווח הנקי השנתי עולה על כ-250,000 ש"ח, או כאשר העסק מעסיק עובדים ונחשף לסיכונים משפטיים וחוזיים משמעותיים המצריכים הגנה על הרכוש הפרטי.</p>
        """,
        'contentEn': """
            <p>Every entrepreneur establishing a business in Israel faces a foundational structural choice: registering as a Sole Proprietorship (Osek Murshe) or incorporating as a Limited Company (LTD) at the Corporations Authority.</p>
            
            <h2>1. Legal Liability and the Corporate Veil</h2>
            <p>This is the most critical distinction:
            * **Sole Proprietorship**: No legal separation exists. Owners are personally liable for all business debts.
            * **LTD Company**: A company is a separate legal entity. The "corporate veil" protects shareholders\' personal assets from business creditors.</p>
            
            <h2>2. Taxation and Corporate Brand Image</h2>
            <p>LTD companies pay a flat corporate tax (23% in 2026), whereas sole proprietors pay progressive personal income taxes up to 50%. Incorporating also project status to institutional clients.</p>
            
            <h2>When is the Right Time to Incorporate?</h2>
            <p>As a rule of thumb, incorporation becomes financially viable when annual net profits exceed 250,000 NIS, or when the business hires employees and faces operational liabilities.</p>
        """
    },
    {
        'slug': 'nonprofit-association-establishment-israel',
        'practiceAreaId': 'corporate-non-profit-registration',
        'image': 'article_company_3.png',
        'date': '01.01.2026',
        'readTime': '5 min read',
        'categoryHe': 'רישום חברות ועמותות',
        'categoryEn': 'Corporate & Non-Profit',
        'titleHe': 'הקמת עמותה צעד אחר צעד: מרישום ברשם העמותות ועד אישור ניהול תקין',
        'titleEn': 'Establishing a Non-Profit Association (Amuta) in Israel: Step-by-Step Legal Guide',
        'descHe': 'תקנון, מוסדות העמותה, והדרך לקבלת אישור ניהול תקין וסעיף 46 לצורך גיוס תרומות.',
        'descEn': 'Bylaws, internal corporate bodies, and pathways to securing Section 46 tax-exempt status for fundraising.',
        'contentHe': """
            <p>הקמת עמותה בישראל היא הדרך המשפטית הנכונה לניהול פעילות ציבורית, חברתית, דתית או חינוכית ללא מטרות רווח (מלכ"ר). ניהול עמותה דורש עמידה בכללים רגולטוריים נוקשים מול רשם העמותות במשרד המשפטים.</p>
            
            <h2>שלב 1: הליך הרישום ותקנון העמותה</h2>
            <p>הקמת עמותה דורשת לפחות 7 מייסדים (בני אדם או תאגידים). יש להגיש בקשת רישום לרשם העמותות המפרטת את מטרות העמותה, שמות המייסדים וכתובתה. כמו כן, יש לצרף את תקנון העמותה. ניתן לבחור בתקנון המצוי (תקנון ברירת המחדל של הרשם) או לנסח תקנון מותאם אישית המסדיר את כללי בחירת הוועד, קבלת חברים ואופן ניהול האסיפות.</p>
            
            <h2>שלב 2: מוסדות החובה של העמותה</h2>
            <p>על פי החוק, כל עמותה מחויבת להקים שלושה מוסדות ניהול וביקורת:
            1. **האסיפה הכללית**: המוסד העליון של העמותה המורכב מכלל חברי העמותה.
            2. **הוועד המנהל**: הגוף המנהל את ענייני העמותה השוטפים (לפחות שני חברים).
            3. **ועדת הביקורת**: גוף פנימי המפקח על ניהול ענייני הכספים והתנהלות העמותה על פי החוק.</p>
            
            <h2>שלב 3: הדרך לקבלת אישור ניהול תקין וסעיף 46</h2>
            <p>גיוס תרומות ותמיכות ממשלתיות דורשים קבלת **אישור ניהול תקין** מרשם העמותות (הניתן לאחר שנתיים של פעילות רציפה ודוחות כספיים תקינים). הישג משמעותי נוסף הוא קבלת **אישור סעיף 46 לפקודת מס הכנסה**, המעניק לתורמים לעמותה זיכוי מס בגובה 35% מתרומתם, והוא כלי שיווקי חיוני לגיוס כספים מתורמים ומקרנות בארץ ובעולם.</p>
        """,
        'contentEn': """
            <p>Establishing a non-profit association (Amuta) is the proper legal pathway to run public, educational, or religious activities. Operating an Amuta requires strict adherence to Ministry of Justice regulations.</p>
            
            <h2>Step 1: Registration and Bylaws</h2>
            <p>An association requires a minimum of 7 founding members. You must file registration documents detailing the organization\'s goals and adopt bylaws regulating member meetings and board voting procedures.</p>
            
            <h2>Step 2: Mandatory Association Organs</h2>
            <p>The law requires every association to maintain three organs:
            1. **The General Assembly**: Comprising all members.
            2. **The Executive Board (Va\'ad)**: Managing daily affairs.
            3. **The Audit Committee**: Overseeing compliance and financial checks.</p>
            
            <h2>Step 3: Securing Proper Management Approval and Section 46</h2>
            <p>Fundraising and securing state support require a **Proper Management Certificate** (Nihul Takin). Securing **Section 46 tax-exempt status** grants your donors a 35% tax credit, which is crucial for major donors.</p>
        """
    }
]

# Write HTML Template Function
def get_template(lang, title, desc, category, date, read_time, slug, image, content, practice_area_id):
    if lang == 'he':
        return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | עו״ד אלירם אלגרבלי</title>
  <meta name="description" content="{desc}">
  <link rel="icon" type="image/png" href="../../assets/logo.png">
  <link rel="canonical" href="https://DOMAIN_PLACEHOLDER/articles/{slug}/" />
  <link rel="alternate" hreflang="he-IL" href="https://DOMAIN_PLACEHOLDER/articles/{slug}/" />
  <link rel="alternate" hreflang="en" href="https://DOMAIN_PLACEHOLDER/en/articles/{slug}/" />
  <link rel="alternate" hreflang="x-default" href="https://DOMAIN_PLACEHOLDER/articles/{slug}/" />
  <link rel="stylesheet" href="../../styles/main.css">
</head>
<body id="body-element" class="lang-he">
  <header class="header header-scrolled" id="header">
    <div class="container navbar">
      <a href="../../" class="logo-container">
        <img src="../../assets/logo.png" alt="Logo" class="logo-icon">
        <div class="navbar-logo-text">
          <span lang="he">אלירם אלגרבלי</span>
          <span lang="en">ELIRAM ELGARABLY</span>
          <span class="navbar-logo-subtext">
            <span lang="he">משרד עורכי דין נדל״ן</span>
            <span lang="en">REAL ESTATE LAW FIRM</span>
          </span>
        </div>
      </a>
      <nav>
        <ul class="nav-menu" id="nav-menu">
          <li><a href="../../#about" class="nav-link"><span lang="he">אודות</span><span lang="en">About</span></a></li>
          <li><a href="../../#practice" class="nav-link"><span lang="he">תחומי התמחות</span><span lang="en">Practice Areas</span></a></li>
          <li><a href="../../#calculator" class="nav-link"><span lang="he">סימולטור מס רכישה</span><span lang="en">Tax Simulator</span></a></li>
          <li><a href="../../#yield-calculator" class="nav-link"><span lang="he">מחשבון תשואה</span><span lang="en">Yield Calculator</span></a></li>
          <li><a href="../" class="nav-link active"><span lang="he">מאמרים</span><span lang="en">Articles</span></a></li>
          <li><a href="../../#contact" class="nav-link"><span lang="he">צור קשר</span><span lang="en">Contact</span></a></li>
        </ul>
      </nav>
      <div class="nav-actions">
        <div class="lang-switcher">
          <a href="./" class="lang-btn lang-btn-he active" id="lang-toggle-he">עב</a>
          <span class="lang-divider">|</span>
          <a href="../../en/articles/{slug}/" class="lang-btn lang-btn-en" id="lang-toggle-en">EN</a>
        </div>
        <a href="../../#contact" class="btn btn-gold btn-sm"><span lang="he">ייעוץ ראשוני</span><span lang="en">Consultation</span></a>
      </div>
      <div class="navbar-mobile-actions" style="display: none;">
        <div class="lang-switcher">
          <a href="./" class="lang-btn lang-btn-he">עב</a>
          <a href="../../en/articles/{slug}/" class="lang-btn lang-btn-en">EN</a>
        </div>
        <button class="mobile-nav-toggle" id="mobile-nav-toggle" aria-label="Toggle Navigation">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <main class="article-page-body" style="padding-top: 8rem;">
    <div class="container">
      <div class="article-detail-wrapper">
        <div class="article-detail-hero">
          <img src="../../assets/{image}" alt="{title}">
        </div>
        <div class="article-detail-content">
          <div class="article-detail-meta">
            <a href="../../practice/{practice_area_id}/" class="article-badge" style="position: static; text-decoration: none;">
              <span lang="he">{category}</span>
              <span lang="en">{category}</span>
            </a>
            <span>{date}</span>
            <span class="meta-dot">•</span>
            <span>{read_time}</span>
          </div>

          <h1 class="article-detail-title">
            <span lang="he">{title}</span>
          </h1>

          <div class="article-detail-author-box">
            <div class="author-avatar-wrapper">
              <img src="../../assets/eliram_profile.jpg" alt="עו״ד אלירם אלגרבלי" class="author-avatar">
            </div>
            <div class="author-info">
              <span class="author-name">
                <span lang="he">נכתב על ידי עו״ד אלירם אלגרבלי</span>
              </span>
              <span class="author-title">
                <span lang="he">עורך דין מומחה לנדל"ן ומקרקעין מאז שנת 2013</span>
              </span>
            </div>
          </div>

          <div class="article-body-text">
            {content}
          </div>

          <div class="article-detail-footer">
            <a href="../" class="btn btn-outline btn-sm">
              <span lang="he">← חזרה למאמרים</span>
            </a>
            <!-- BACK_TO_PRACTICE_START -->
            <a href="../../practice/{practice_area_id}/" class="btn btn-outline btn-sm">
              <span lang="he">← לתחום התמחות: {category}</span>
            </a>
            <!-- BACK_TO_PRACTICE_END -->
            <a href="../../#contact" class="btn btn-gold btn-sm">
              <span lang="he">להתייעצות אישית</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container footer-grid">
      <div>
        <div class="logo-container" style="margin-bottom: 1.5rem;">
          <img src="../../assets/logo.png" alt="Logo" class="logo-icon" style="height: 35px; width: 35px;">
          <div class="navbar-logo-text" style="font-size: 1.2rem;">
            <span lang="he">אלירם אלגרבלי</span>
          </div>
        </div>
        <p class="footer-logo-desc">
          משרד בוטיק המתמחה בליווי עסקאות מקרקעין, נדל"ן מסחרי, מיסוי מקרקעין, צוואות וירושות וייפוי כוח מתמשך. מעניקים יחס אישי ומקצועיות ללא פשרות מאז שנת 2013.
        </p>
      </div>
      <div>
        <h4 class="footer-title">ניווט מהיר</h4>
        <ul class="footer-links">
          <li><a href="../../#about" class="footer-link">אודות המשרד</a></li>
          <li><a href="../../#practice" class="footer-link">תחומי התמחות</a></li>
          <li><a href="../../#calculator" class="footer-link">סימולטור מס רכישה</a></li>
          <li><a href="../../#yield-calculator" class="footer-link">מחשבון תשואה מנדל"ן</a></li>
          <li><a href="../" class="footer-link">מאמרים ומדריכים</a></li>
        </ul>
      </div>
      <div>
        <h4 class="footer-title">הבהרה משפטית</h4>
        <p class="footer-logo-desc" style="max-width: 100%; font-size: 0.8rem; opacity: 0.6;">
          המידע המופיע באתר זה מיועד להעשרת הידע הכללי בלבד ואינו מהווה ייעוץ משפטי, חוות דעת משפטית או תחליף לייעוץ פרטני אצל עורך דין מקרקעין מוסמך. הסתמכות על המידע באחריות המשתמש בלבד.
        </p>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container" style="display: flex; justify-content: space-between; align-items: center; width: 100%; flex-wrap: wrap; gap: 1.5rem;">
        <p class="copyright">© 2026 עו״ד אלירם אלגרבלי. כל הזכויות שמורות.</p>
        <div class="footer-legal-links">
          <a href="../../privacy/" class="footer-link" style="font-size: 0.85rem;">מדיניות פרטיות</a>
          <span style="opacity: 0.3;">|</span>
          <a href="../../disclaimer/" class="footer-link" style="font-size: 0.85rem;">הבהרה משפטית</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="../../js/main.js"></script>
</body>
</html>
"""
    else:
        return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Adv. Eliram Elgarably</title>
  <meta name="description" content="{desc}">
  <link rel="icon" type="image/png" href="../../../assets/logo.png">
  <link rel="canonical" href="https://DOMAIN_PLACEHOLDER/en/articles/{slug}/" />
  <link rel="alternate" hreflang="he-IL" href="https://DOMAIN_PLACEHOLDER/articles/{slug}/" />
  <link rel="alternate" hreflang="en" href="https://DOMAIN_PLACEHOLDER/en/articles/{slug}/" />
  <link rel="alternate" hreflang="x-default" href="https://DOMAIN_PLACEHOLDER/articles/{slug}/" />
  <link rel="stylesheet" href="../../../styles/main.css">
</head>
<body id="body-element" class="lang-en">
  <header class="header header-scrolled" id="header">
    <div class="container navbar">
      <a href="../../" class="logo-container">
        <img src="../../../assets/logo.png" alt="Logo" class="logo-icon">
        <div class="navbar-logo-text">
          <span lang="he">אלירם אלגרבלי</span>
          <span lang="en">ELIRAM ELGARABLY</span>
          <span class="navbar-logo-subtext">
            <span lang="he">משרד עורכי דין נדל״ן</span>
            <span lang="en">REAL ESTATE LAW FIRM</span>
          </span>
        </div>
      </a>
      <nav>
        <ul class="nav-menu" id="nav-menu">
          <li><a href="../../#about" class="nav-link"><span lang="he">אודות</span><span lang="en">About</span></a></li>
          <li><a href="../../#practice" class="nav-link"><span lang="he">תחומי התמחות</span><span lang="en">Practice Areas</span></a></li>
          <li><a href="../../#calculator" class="nav-link"><span lang="he">סימולטור מס רכישה</span><span lang="en">Tax Simulator</span></a></li>
          <li><a href="../../#yield-calculator" class="nav-link"><span lang="he">מחשבון תשואה</span><span lang="en">Yield Calculator</span></a></li>
          <li><a href="../" class="nav-link active"><span lang="he">מאמרים</span><span lang="en">Articles</span></a></li>
          <li><a href="../../#contact" class="nav-link"><span lang="he">צור קשר</span><span lang="en">Contact</span></a></li>
        </ul>
      </nav>
      <div class="nav-actions">
        <div class="lang-switcher">
          <a href="../../../articles/{slug}/" class="lang-btn lang-btn-he" id="lang-toggle-he">עב</a>
          <span class="lang-divider">|</span>
          <a href="./" class="lang-btn lang-btn-en active" id="lang-toggle-en">EN</a>
        </div>
        <a href="../../#contact" class="btn btn-gold btn-sm"><span lang="he">ייעוץ ראשוני</span><span lang="en">Consultation</span></a>
      </div>
      <div class="navbar-mobile-actions" style="display: none;">
        <div class="lang-switcher">
          <a href="../../../articles/{slug}/" class="lang-btn lang-btn-he">עב</a>
          <a href="./" class="lang-btn lang-btn-en active">EN</a>
        </div>
        <button class="mobile-nav-toggle" id="mobile-nav-toggle" aria-label="Toggle Navigation">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <main class="article-page-body" style="padding-top: 8rem;">
    <div class="container">
      <div class="article-detail-wrapper">
        <div class="article-detail-hero">
          <img src="../../../assets/{image}" alt="{title}">
        </div>
        <div class="article-detail-content">
          <div class="article-detail-meta">
            <a href="../../practice/{practice_area_id}/" class="article-badge" style="position: static; text-decoration: none;">
              <span lang="en">{category}</span>
            </a>
            <span>{date}</span>
            <span class="meta-dot">•</span>
            <span>{read_time}</span>
          </div>

          <h1 class="article-detail-title">
            <span lang="en">{title}</span>
          </h1>

          <div class="article-detail-author-box">
            <div class="author-avatar-wrapper">
              <img src="../../../assets/eliram_profile.jpg" alt="Adv. Eliram Elgarably" class="author-avatar">
            </div>
            <div class="author-info">
              <span class="author-name">
                <span lang="en">Written by Adv. Eliram Elgarably</span>
              </span>
              <span class="author-title">
                <span lang="en">Real Estate Law Specialist practicing since 2013</span>
              </span>
            </div>
          </div>

          <div class="article-body-text">
            {content}
          </div>

          <div class="article-detail-footer">
            <a href="../" class="btn btn-outline btn-sm">
              <span lang="en">← Back to Articles</span>
            </a>
            <!-- BACK_TO_PRACTICE_START -->
            <a href="../../../en/practice/{practice_area_id}/" class="btn btn-outline btn-sm">
              <span lang="en">← Practice Area: {category}</span>
            </a>
            <!-- BACK_TO_PRACTICE_END -->
            <a href="../../#contact" class="btn btn-gold btn-sm">
              <span lang="en">Get Advice</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container footer-grid">
      <div>
        <div class="logo-container" style="margin-bottom: 1.5rem;">
          <img src="../../../assets/logo.png" alt="Logo" class="logo-icon" style="height: 35px; width: 35px;">
          <div class="navbar-logo-text" style="font-size: 1.2rem;">
            <span lang="en">ELIRAM ELGARABLY</span>
          </div>
        </div>
        <p class="footer-logo-desc">
          Boutique law firm specializing in real estate deals, commercial property, property taxation, wills, and ongoing POA. Serving clients with excellence since 2013.
        </p>
      </div>
      <div>
        <h4 class="footer-title">Quick Links</h4>
        <ul class="footer-links">
          <li><a href="../../#about" class="footer-link">About the Firm</a></li>
          <li><a href="../../#practice" class="footer-link">Practice Areas</a></li>
          <li><a href="../../#calculator" class="footer-link">Purchase Tax Simulator</a></li>
          <li><a href="../../#yield-calculator" class="footer-link">Yield Calculator</a></li>
          <li><a href="../" class="footer-link">Articles &amp; Guides</a></li>
        </ul>
      </div>
      <div>
        <h4 class="footer-title">Legal Disclaimer</h4>
        <p class="footer-logo-desc" style="max-width: 100%; font-size: 0.8rem; opacity: 0.6;">
          The contents of this website are provided for general educational purposes only, and do not constitute formal legal advice or opinion, nor do they replace personalized consultation with a qualified real estate attorney.
        </p>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container" style="display: flex; justify-content: space-between; align-items: center; width: 100%; flex-wrap: wrap; gap: 1.5rem;">
        <p class="copyright">© 2026 Adv. Eliram Elgarably. All rights reserved.</p>
        <div class="footer-legal-links">
          <a href="../../privacy/" class="footer-link" style="font-size: 0.85rem;">Privacy Policy</a>
          <span style="opacity: 0.3;">|</span>
          <a href="../../disclaimer/" class="footer-link" style="font-size: 0.85rem;">Disclaimer</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="../../../js/main.js"></script>
</body>
</html>
"""

if __name__ == '__main__':
    print("Starting article files generation...")
    # Ensure asset directory exists
    assets_dir = os.path.join(BASE_DIR, 'assets')
    os.makedirs(assets_dir, exist_ok=True)
    
    # Map practice area id to base image name
    area_to_base_image = {
        'second-hand-property': 'article_second_hand_base.png',
        'new-contractor-purchase': 'article_contractor_base.png',
        'urban-renewal': 'article_urban_base.png',
        'real-estate-taxation': 'article_tax_base.png',
        'commercial-properties': 'article_commercial_base.png',
        'partnerships-coownership': 'article_partnership_base.png',
        'wills-inheritance': 'article_wills_base.png',
        'ongoing-power-of-attorney': 'article_poa_base.png',
        'corporate-non-profit-registration': 'article_company_base.png'
    }
    
    for article in ARTICLES_DATA:
        slug = article['slug']
        area_id = article['practiceAreaId']
        image_name = article['image']
        
        # Determine Hebrew and English paths
        he_dir = os.path.join(ARTICLES_DIR, slug)
        en_dir = os.path.join(EN_ARTICLES_DIR, slug)
        
        os.makedirs(he_dir, exist_ok=True)
        os.makedirs(en_dir, exist_ok=True)
        
        # Write Hebrew HTML
        he_html = get_template(
            lang='he',
            title=article['titleHe'],
            desc=article['descHe'],
            category=article['categoryHe'],
            date=article['date'],
            read_time=article['readTime'],
            slug=slug,
            image=image_name,
            content=article['contentHe'],
            practice_area_id=area_id
        )
        with open(os.path.join(he_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(he_html)
            
        # Write English HTML
        en_html = get_template(
            lang='en',
            title=article['titleEn'],
            desc=article['descEn'],
            category=article['categoryEn'],
            date=article['date'],
            read_time=article['readTime'],
            slug=slug,
            image=image_name,
            content=article['contentEn'],
            practice_area_id=area_id
        )
        with open(os.path.join(en_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(en_html)
            
        # Copy base image to specific article image filename if it exists
        base_img_name = area_to_base_image.get(area_id)
        if base_img_name:
            src_path = os.path.join(assets_dir, base_img_name)
            dst_path = os.path.join(assets_dir, image_name)
            if os.path.exists(src_path):
                shutil.copy2(src_path, dst_path)
                print(f"Copied {base_img_name} to {image_name}")
            else:
                print(f"Warning: Base image {base_img_name} not found in assets. Make sure it is generated.")
                
        print(f"Generated Hebrew and English pages for slug: {slug}")
    print("All article files generated successfully.")

