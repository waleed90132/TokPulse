import json
import random
import uuid
import urllib.request
import urllib.parse
import time
from datetime import datetime

# =========================================================================
# 1. محرك سحب الصوتيات والأغاني الحية من Apple Music (200+ فنان)
# =========================================================================
GENRE_QUERIES = {
    "خليجي / فخامة": ["عبدالمجيد عبدالله", "راشد الماجد", "محمد عبده", "ماجد المهندس", "رابح صقر", "دحوم الطلاسي", "عايض يوسف", "متعب الشعلان"],
    "شيلات / حماسي": ["فهد بن فصلا", "بدر العزي", "غريب ال مخلص", "عبدالله ال مخلص", "ماجد الرسلاني", "نادر الشراري", "شبل الدواسر", "فهد العيباني"],
    "ترند / بوب عربي": ["الشامي", "السيلاوي", "احمد سعد", "عمرو دياب", "تامر حسني", "سعد لمجرد", "حسين الجسمي", "بلقيس", "محمود التركي", "رحمة رياض"],
    "راب / تراب": ["ويجز", "مروان بابلو", "عفروتو", "مروان موسى", "مسلم", "عصام صاصا", "ديسكو مصر", "سولكينغ", "بلطي", "فليبراتشي"],
    "روقان / لوفاي": ["عزف عود", "عمر خيرت", "نصير شمة", "عبادي الجوهر", "Lofi Arabic", "تقاسيم عود هادئة", "بيانو عربي", "موسيقى نوم واسترخاء"],
    "دبكات / طرب": ["دبكات 2026", "ريمكس عراقي دمار", "دبكة مجوز ثقيل", "ريمكس عربي مسرع", "سيف نبيل", "ناصيف زيتون"],
    "ديكور / روقان": ["موسيقى روقان", "Chill Arabic", "تقاسيم عود هادئة", "عزف قانون شرقي", "Lofi Beats Chill"],
    "تجارة / بزنس": ["موسيقى اعلانات", "تحفيز اعمال", "نجاح وطاقة", "موسيقى الكترونية عربية", "Epic Beats Business"],
    "سيارات / هجولة": ["شيلات مسرعة", "شيلة خط", "ريمكس هجولة دمار", "دريفت مسرع طرب", "شيلات حماسية دقات"],
    "رياضة / جيم": ["حماس جيم", "ريمكس رياضة", "تحفيز رياضي", "Workout Arabic Remix", "حماس ملاكمة وبادل"],
    "فلوق / يوميات": ["اغاني روقان تيك توك", "كافيهات صباحية", "موسيقى فلوقات عربية", "هدوء الصباح قهوة"]
}

def generate_live_sounds():
    all_sounds = []
    used_tracks = set()
    print("🎵 1. جاري جلب 50 صوتاً وأغنية حقيقية من Apple Music...")

    for category, terms in GENRE_QUERIES.items():
        term = random.choice(terms)
        try:
            country = random.choice(["sa", "ae", "eg"])
            encoded_term = urllib.parse.quote(term)
            url = f"https://itunes.apple.com/search?term={encoded_term}&limit=12&media=music&country={country}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            
            with urllib.request.urlopen(req, timeout=6) as response:
                data = json.loads(response.read().decode('utf-8'))
                results = data.get("results", [])
                for item in results:
                    track = item.get("trackName")
                    artist = item.get("artistName")
                    preview = item.get("previewUrl")
                    if track and artist and preview and preview.startswith("http"):
                        key = f"{artist} - {track}"
                        if key not in used_tracks:
                            used_tracks.add(key)
                            uses = round(random.uniform(25.0, 990.0), 1)
                            growth = random.randint(350, 1600)
                            fire_emoji = "🔥" if growth > 750 else "📈"
                            clean_q = urllib.parse.quote(f"{artist} {track}")
                            all_sounds.append({
                                "id": str(uuid.uuid4())[:8],
                                "title": f"صوت: {track} 🎵",
                                "author": artist,
                                "usesCount": f"+{uses}K استخدام",
                                "growthRate": f"{fire_emoji} نمو +{growth}% اليوم",
                                "previewAudioUrl": preview,
                                "officialUrl": f"https://www.tiktok.com/search?q={clean_q}",
                                "category": category
                            })
            time.sleep(0.08)
        except Exception as e:
            print(f"تنبيه بالصوتيات ({term}): {e}")

    random.shuffle(all_sounds)
    return all_sounds[:50]

# =========================================================================
# 2. محرك هاشتاجات الدول وترندات المنطقة (Country Trends)
# =========================================================================
COUNTRIES_MASTER_DATA = {
    "KW": {
        "name": "الكويت 🇰🇼",
        "tags": [
            ("#الكويت", "+8.9B", "🔥 متصدر الآن"), ("#ترند_الكويت", "+4.2B", "🔥 متصدر الآن"),
            ("#المطلاع", "+920M", "🚀 نمو سريع"), ("#كافيهات_الكويت", "+1.4B", "📈 صاعد"),
            ("#ديكور_الكويت", "+780M", "📈 صاعد"), ("#سيارات_الكويت", "+1.1B", "🔥 متصدر الآن"),
            ("#اعلانات_الكويت", "+2.1B", "🚀 نمو سريع"), ("#غبقة_الكويت", "+640M", "📈 صاعد"),
            ("#ديوانية", "+890M", "📈 صاعد"), ("#مطاعم_الكويت", "+3.5B", "🔥 متصدر الآن"),
            ("#سوق_الكويت", "+1.8B", "🚀 نمو سريع"), ("#قسائم_الكويت", "+450M", "📈 صاعد")
        ]
    },
    "SA": {
        "name": "السعودية 🇸🇦",
        "tags": [
            ("#السعودية", "+45.2B", "🔥 متصدر الآن"), ("#الرياض", "+18.4B", "🔥 متصدر الآن"),
            ("#جدة", "+12.1B", "🔥 متصدر الآن"), ("#موسم_الرياض", "+6.8B", "🚀 نمو سريع"),
            ("#كشتات", "+3.1B", "📈 صاعد"), ("#عقارات_الرياض", "+2.4B", "🚀 نمو سريع"),
            ("#بنات_الرياض", "+5.6B", "🔥 متصدر الآن"), ("#شيلات_حماسية", "+4.9B", "🔥 متصدر الآن"),
            ("#يوم_التأسيس", "+7.2B", "🚀 نمو سريع"), ("#الشرقية", "+4.1B", "📈 صاعد"),
            ("#تطوير_الذات", "+3.8B", "📈 صاعد"), ("#تجارة_الكترونية_السعودية", "+1.9B", "🚀 نمو سريع")
        ]
    },
    "AE": {
        "name": "الإمارات 🇦🇪",
        "tags": [
            ("#دبي", "+22.6B", "🔥 متصدر الآن"), ("#الامارات", "+14.8B", "🔥 متصدر الآن"),
            ("#ابوظبي", "+8.4B", "🔥 متصدر الآن"), ("#DubaiLife", "+12.9B", "🔥 متصدر الآن"),
            ("#عقارات_دبي", "+4.1B", "🚀 نمو سريع"), ("#مطاعم_دبي", "+3.9B", "📈 صاعد"),
            ("#برج_خليفة", "+6.2B", "📈 صاعد"), ("#سياحة_الامارات", "+2.8B", "🚀 نمو سريع"),
            ("#سيارات_دبي", "+5.1B", "🔥 متصدر الآن"), ("#بزنس_دبي", "+1.7B", "🚀 نمو سريع")
        ]
    },
    "EG": {
        "name": "مصر 🇪🇬",
        "tags": [
            ("#مصر", "+38.4B", "🔥 متصدر الآن"), ("#القاهرة", "+11.2B", "🔥 متصدر الآن"),
            ("#الاسكندرية", "+6.7B", "📈 صاعد"), ("#كوميديا_مصرية", "+9.4B", "🔥 متصدر الآن"),
            ("#الساحل_الشمالي", "+4.8B", "🚀 نمو سريع"), ("#اكلات_مصرية", "+5.2B", "📈 صاعد"),
            ("#دراما_مصرية", "+7.1B", "🔥 متصدر الآن"), ("#شغل_اونلاين_مصر", "+2.3B", "🚀 نمو سريع"),
            ("#تيك_توك_مصر", "+15.6B", "🔥 متصدر الآن"), ("#شباب_مصر", "+4.4B", "📈 صاعد")
        ]
    },
    "QA": {
        "name": "قطر 🇶🇦",
        "tags": [
            ("#قطر", "+9.8B", "🔥 متصدر الآن"), ("#الدوحة", "+5.4B", "🔥 متصدر الآن"),
            ("#سوق_واقف", "+1.6B", "📈 صاعد"), ("#مطاعم_قطر", "+2.1B", "🚀 نمو سريع"),
            ("#لوسيل", "+1.9B", "📈 صاعد"), ("#فعاليات_قطر", "+1.2B", "🚀 نمو سريع")
        ]
    },
    "US": {
        "name": "أمريكا والعالم 🌍",
        "tags": [
            ("#fyp", "+1280B", "🔥 متصدر الآن"), ("#viral", "+890B", "🔥 متصدر الآن"),
            ("#TikTokMadeMeBuyIt", "+110B", "🔥 متصدر الآن"), ("#trending", "+450B", "🔥 متصدر الآن"),
            ("#lifehacks", "+95B", "🚀 نمو سريع"), ("#tech", "+78B", "📈 صاعد"),
            ("#dropshipping", "+34B", "🚀 نمو سريع"), ("#business", "+62B", "📈 صاعد")
        ]
    }
}

def generate_country_trends():
    print("🌍 2. جاري تنظيم هاشتاجات الدول وترندات الخليج ومصر...")
    country_result = {}
    for code, data in COUNTRIES_MASTER_DATA.items():
        shuffled_tags = data["tags"].copy()
        random.shuffle(shuffled_tags)
        formatted_list = []
        for tag, views, status in shuffled_tags:
            growth_pct = random.randint(120, 850)
            encoded_tag = urllib.parse.quote(tag)
            formatted_list.append({
                "id": str(uuid.uuid4())[:8],
                "tag": tag,
                "views": views,
                "status": status,
                "growthRate": f"+{growth_pct}%",
                "searchUrl": f"https://www.tiktok.com/tag/{encoded_tag.replace('#', '')}"
            })
        country_result[code] = {
            "countryName": data["name"],
            "tags": formatted_list
        }
    return country_result

# =========================================================================
# 3. محرك صائد المنتجات الرابحة (Winning Dropshipping Products)
# =========================================================================
WINNING_PRODUCTS_POOL = [
    {
        "name": "ماكينة إزالة وبر الملابس والأثاث اللاسلكية 🧽",
        "niche": "أجهزة منزلية وعناية",
        "problem": "إعادة الملابس والكنب القديم كالجديد بـ 30 ثانية بدون إتلاف القماش",
        "profit_angle": "هامش ربح يتجاوز 65%، فيديو المقارنة قبل وبعد بحقق ملايين المشاهدات",
        "query": "Fabric Shaver Lint Remover Viral"
    },
    {
        "name": "موزع زيت الشعر وفروة الرأس الذكي بالسيليكون 💆‍♀️",
        "niche": "جمال وعناية شخصية",
        "problem": "توزيع زيوت وسيروم الشعر مباشرة للجذور بدون توسيخ اليدين أو هدر الزيت",
        "profit_angle": "ترند تيك توك شوب متصدر في الخليج، سهل البيع كباقة مع زيوت طبيعية",
        "query": "Scalp Oil Applicator Massager"
    },
    {
        "name": "إضاءة الليد المغناطيسية بحساس الحركة للدواليب 💡",
        "niche": "ديكور وإضاءة ذكية",
        "problem": "إنارة الخزائن والممرات المظلمة بدون حفر أو تمديد أسلاك كهربائية",
        "profit_angle": "العميل بشتري بالعادة 3 إلى 5 حبات للمنزل الواحد (Upsell عالي)",
        "query": "Wireless Under Cabinet Motion Sensor Light"
    },
    {
        "name": "مضخة غسيل السيارات اللاسلكية بالضغط العالي 🚗",
        "niche": "سيارات وتلميع",
        "problem": "غسيل السيارة في أي مكان بدون الحاجة لمصدر ماء أو كهرباء ثابت",
        "profit_angle": "منتج فخم بمعدل مبيعات مرتفع لعشاق السيارات والكشتات",
        "query": "Cordless High Pressure Car Washer"
    },
    {
        "name": "حامل الهاتف المغناطيسي الذكي مع تتبع الوجه 360° 📱",
        "niche": "صناعة محتوى وتقنية",
        "problem": "تصوير فيديوهات تيك توك احترافية وتتبع حركتك تلقائياً بدون مصور",
        "profit_angle": "مطلوب بقوة من صناع المحتوى والمدربين والمعلمين أونلاين",
        "query": "Auto Face Tracking Phone Holder 360"
    },
    {
        "name": "مرطب الجو المضاد للجاذبية بقطرات الماء الصاعدة 💧",
        "niche": "ديكور وسيت أب",
        "problem": "ترطيب الغرفة بشكل بصري ساحر وجذاب يلفت الأنظار بالمكتب والصالة",
        "profit_angle": "منتج فايرال كوري جذاب بصرياً بالثواني الأولى من الفيديو",
        "query": "Anti Gravity Water Droplet Humidifier"
    },
    {
        "name": "فرشاة تنظيف الأطباق الكهربائية الدوارة 5 في 1 🍳",
        "niche": "أدوات مطبخ وتنظيف",
        "problem": "تنظيف أصعب دهون المطبخ والبلاط بضغطة زر وبدون مجهود يدوي",
        "profit_angle": "حل سحري لربات البيوت، يسهل تسويقه بفيديو مقارنة عملي",
        "query": "Electric Spin Scrubber Kitchen Cleaner"
    },
    {
        "name": "مسند تصحيح الظهر والعمود الفقري الذكي مع هزاز 🧘‍♂️",
        "niche": "صحة ولياقة",
        "problem": "التنبيه بالاهتزاز فور انحناء الظهر لعلاج آلام الرقبة والمكتب",
        "profit_angle": "يحل مشكلة شائعة لملايين الموظفين والطلاب واللاعبين",
        "query": "Smart Posture Corrector Vibration Sensor"
    },
    {
        "name": "شاحن لاسلكي 3 في 1 قابل للطي بتصميم شفاف ⚡",
        "niche": "اكسسوارات هواتف وسفر",
        "problem": "شحن الآيفون والساعة والسماعة بسلك واحد مدمج أثناء السفر والمكتب",
        "profit_angle": "شكل نيون عصري فخم وسهل الاستهداف لأصحاب أجهزة أبل",
        "query": "Foldable 3 in 1 Wireless Charger Station"
    },
    {
        "name": "قاطع ومبشرة الخضار اليدوية الدوارة السريعة 🥗",
        "niche": "مطبخ وأدوات طعام",
        "problem": "تقطيع الخضار والمكسرات والجبن بـ 5 ثواني وبأمان تام للأصابع",
        "profit_angle": "منتج متصدر مبيعات تيك توك شوب دائماً بسبب سرعة العرض بالفيديو",
        "query": "Rotary Vegetable Cheese Grater Shredder"
    },
    {
        "name": "مظلة الزجاج الأمامي للسيارة القابلة للطي ☀️",
        "niche": "سيارات وحماية الصيف",
        "problem": "عزل حرارة شمس الصيف الحارقة بالخليج وحماية طبلون السيارة",
        "profit_angle": "منتج صيفي ضروري وسريع المبيعات في الكويت والسعودية والإمارات",
        "query": "Foldable Car Windshield Sun Shade Umbrella"
    },
    {
        "name": "سماعة النوم اللاسلكية المدمجة بقناع العين ثلاثي الأبعاد 💤",
        "niche": "راحة ونوم عميق",
        "problem": "النوم في الطائرة أو الغرفة المعتمة مع الاستماع للمدائح أو البودكاست براحة",
        "profit_angle": "يستهدف الباحثين عن النوم العميق وعشاق السفر والبيلوكس",
        "query": "Bluetooth Eye Mask Sleep Headphones 3D"
    }
]

def generate_winning_products():
    print("📦 3. جاري توليد صائد منتجات التجارة والدروب شيبينغ...")
    shuffled = WINNING_PRODUCTS_POOL.copy()
    random.shuffle(shuffled)
    products = []
    
    for item in shuffled:
        growth = random.randint(280, 1450)
        orders = random.randint(1200, 48000)
        encoded_q = urllib.parse.quote(item["query"])
        products.append({
            "id": str(uuid.uuid4())[:8],
            "productName": item["name"],
            "niche": item["niche"],
            "problemSolved": item["problem"],
            "profitAngle": item["profit_angle"],
            "estimatedOrders": f"+{orders:,} طلب",
            "growthRate": f"🔥 +{growth}% هذا الأسبوع",
            "tiktokAdsUrl": f"https://www.tiktok.com/search?q={encoded_q}",
            "supplierSearchUrl": f"https://www.aliexpress.com/wholesale?SearchText={encoded_q}"
        })
    return products

# =========================================================================
# 4. محرك صائد الأسئلة الفيروسية من التعليقات (Viral Q&A Hunter)
# =========================================================================
VIRAL_QUESTIONS_POOL = [
    {"question": "كم كلفكم المتر عظم بالتشطيب مع المواد؟ 💰", "niche": "ديكور وتشطيبات 🛋️", "difficulty": "سهل (تفاعل صاروخي)"},
    {"question": "ليش بطلت تستخدم فلاتر بوجهك بالفيديوهات؟ 👁️", "niche": "صناعة محتوى 📱", "difficulty": "متوسط (فضول عالي)"},
    {"question": "كيف فتحت متجرك بـ 100 دينار وطلعت أرباح أول شهر؟ 🚀", "niche": "تجارة وبزنس 📈", "difficulty": "شديد الجذب 🧲"},
    {"question": "شو الفرق الحقيقي بين رندر V-Ray و D5 Render بالواقعية؟ 🎨", "niche": "تصميم وجرافيك 🎨", "difficulty": "نقاش تقني دسم"},
    {"question": "إذا بدأت برمجة من الصفر بالذكاء الاصطناعي كم أحتاج وقت؟ 🤖", "niche": "برمجة وذكاء 💻", "difficulty": "تفاعل تعليمي"},
    {"question": "ليش إضاءة 3000K أحسن من الإضاءة البيضاء للصالات؟ 💡", "niche": "ديكور وإضاءة 🛋️", "difficulty": "جدلي ومقنع"},
    {"question": "كيف تتصرف إذا العميل عملك بلوك بعد ما سلمته المشروع؟ 😡", "niche": "عمل حر وبزنس ⏳", "difficulty": "قصة وسرد تجارب"},
    {"question": "شو السبب اللي بخلي المشاهدات تعلق عند 200 مشاهدة بتيك توك؟ 🛑", "niche": "خوارزميات 📱", "difficulty": "سؤال الموسم 🔥"},
    {"question": "هل الشاحن التجاري الرخيص فعلاً بحرق بطارية الآيفون؟ ⚡", "niche": "تقنية وهواتف 💻", "difficulty": "تحذيري صادم"},
    {"question": "كيف تنزل وزنك بدون ما تحرم حالك من أكل المطاعم؟ 🍔", "niche": "صحة ورشاقة 🏋️", "difficulty": "تفاعل عالي جداً"},
    {"question": "شو أفضل رد لما العميل يحكيلك (سعرك غالي ولقيت أرخص)؟ 🗣️", "niche": "مبيعات وتسويق 📈", "difficulty": "فن إغلاق الصفقات"},
    {"question": "كيف تشتري سيارة مستعملة بدون ما ينضحك عليك بالصبغ والحوادث؟ 🚗", "niche": "سيارات وفحص 🏎️", "difficulty": "قيمة وإنقاذ مالي"}
]

def generate_viral_questions():
    print("❓ 4. جاري تجهيز صائد الأسئلة الفيروسية للأفكار...")
    shuffled = VIRAL_QUESTIONS_POOL.copy()
    random.shuffle(shuffled)
    questions = []
    for q in shuffled:
        views_boost = random.randint(40, 190)
        questions.append({
            "id": str(uuid.uuid4())[:8],
            "question": q["question"],
            "niche": q["niche"],
            "viralRating": q["difficulty"],
            "estimatedReachBoost": f"+{views_boost}% تفاعل متوقع",
            "suggestedHook": f"أكثر سؤال وصلني بالتعليقات: {q['question']}.. وهي الجواب الصادم!",
            "actionPrompt": "افتح الكاميرا واقرأ السؤال من الشاشة ورد عليه مباشرة بثقة."
        })
    return questions

# =========================================================================
# 5. بنك الإفيهات والكومنتات الأكثر تفاعلاً (Top Viral Comments)
# =========================================================================
TOP_COMMENTS_POOL = [
    {"comment": "السر مش بالمنتج، السر بالزاوية اللي بتصور منها 🤫✨", "type": "حكمة وتسويق", "likes": "+18.4K"},
    {"comment": "المقاول الشاطر ببين من نعلات الأرضية والزوايا مش من دهان الصالة! 🧱👌", "type": "قصف جبهات هندسي", "likes": "+24.2K"},
    {"comment": "دخلت عشان أتعلم كيف أوفر، طلعت شاري المنتج وأنا بضحك! 😂💸", "type": "كوميدي وفايرال", "likes": "+35.1K"},
    {"comment": "التيك توك بحسسك إنه كل الناس صارت مليونيرية إلا أنت وصاحبك! 🌚", "type": "واقعي ساخر", "likes": "+41.8K"},
    {"comment": "احفظ الفيديو هسا لأنك رح ترجع تدور عليه وتندم وقت التشطيب! 📌💎", "type": "كول تو أكشن مغناطيسي", "likes": "+15.9K"},
    {"comment": "العميل اللي بفاصلك على 5 دنانير هو أول واحد بطلب 50 تعديل! 🤦‍♂️", "type": "معاناة الفريلانسرز", "likes": "+29.7K"},
    {"comment": "إذا التطبيق مجاني 100%، تأكد إنك أنت المنتج اللي بنباع يا صديقي! 👁️", "type": "صدمة ووعي تقني", "likes": "+52.3K"},
    {"comment": "أنا ما بنافس بالسعر، أنا بنافس براحة بالك وجودة الشغل اللي رح تعيش معك عمر! 💎👑", "type": "رد مبيعات ملكي", "likes": "+21.0K"},
    {"comment": "الفيديو طلعلي بالوقت المناسب بالضبط، جاري التطبيق فوراً! 🚀🔥", "type": "تفاعل إيجابي", "likes": "+12.6K"},
    {"comment": "خوارزمية تيك توك بتعرف عني أكثر من أهلي والله! 😂🎯", "type": "ميمز وترند", "likes": "+38.4K"}
]

def generate_top_comments():
    print("💬 5. جاري توليد بنك الكومنتات والإفيهات الذكية...")
    shuffled = TOP_COMMENTS_POOL.copy()
    random.shuffle(shuffled)
    comments = []
    for c in shuffled:
        comments.append({
            "id": str(uuid.uuid4())[:8],
            "commentText": c["comment"],
            "commentType": c["type"],
            "engagementLikes": c["likes"],
            "copyAdvice": "انسخ هذا التعليق وضعه على فيديوهات منافسيك لجذب زيارات لبروفايلك."
        })
    return comments

# =========================================================================
# 6. بوصلة أفضل أوقات النشر الجغرافية (Best Posting Times)
# =========================================================================
def generate_posting_times():
    print("⏰ 6. جاري إعداد بوصلة أفضل ساعات النشر للخليج والعالم...")
    return {
        "KW_SA_QA": {
            "regionName": "الكويت، السعودية، قطر (توقيت مكة GMT+3)",
            "goldenHours": [
                {"slot": "فترة الظهيرة والراحة ☀️", "time": "01:15 PM - 02:45 PM", "engagement": "92% تفاعل عالي"},
                {"slot": "ذروة المساء الذهبية 🌙", "time": "08:30 PM - 11:30 PM", "engagement": "98% أعلى قمة تفاعل"},
                {"slot": "سهرة وسوالف آخر الليل 🌚", "time": "12:45 AM - 02:00 AM", "engagement": "86% روقان ومقاطع طويلة"}
            ],
            "bestDays": "الخميس والجمعة والسبت (عطلة نهاية الأسبوع)"
        },
        "AE": {
            "regionName": "الإمارات وسلطنة عمان (GMT+4)",
            "goldenHours": [
                {"slot": "استراحة الغداء 🏙️", "time": "02:00 PM - 03:30 PM", "engagement": "89% نشاط موظفين"},
                {"slot": "فترة ما بعد العشاء 🌆", "time": "09:00 PM - 11:45 PM", "engagement": "97% ذروة التصفح"},
                {"slot": "صباحيات القهوة ☕", "time": "08:00 AM - 09:30 AM", "engagement": "81% تصفح سريع"}
            ],
            "bestDays": "الجمعة والسبت والأحد"
        },
        "EG": {
            "regionName": "مصر وبلاد الشام (GMT+3)",
            "goldenHours": [
                {"slot": "بعد العصر والمواصلات 🚌", "time": "04:30 PM - 06:00 PM", "engagement": "88% رجوع من الدوام"},
                {"slot": "سهرة المساء الكبرى ☕", "time": "09:30 PM - 01:00 AM", "engagement": "99% أعلى نشاط مشاهدات"}
            ],
            "bestDays": "الخميس والجمعة"
        }
    }

# =========================================================================
# المحرك الرئيسي: بناء ملف data.json الموسوعي الشامل
# =========================================================================
def build_master_payload():
    start_time = time.time()
    print("=" * 60)
    print("🚀 بدء تشغيل محرك TokPulse Master Data Generator...")
    print("=" * 60)

    payload = {
        "version": int(datetime.now().strftime("%Y%m%d%H")),
        "lastUpdated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sounds": generate_live_sounds(),
        "country_trends": generate_country_trends(),
        "winning_products": generate_winning_products(),
        "viral_questions": generate_viral_questions(),
        "top_comments": generate_top_comments(),
        "posting_times": generate_posting_times()
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    elapsed = round(time.time() - start_time, 2)
    print("=" * 60)
    print(f"🎉 تم بنجاح إنشاء وتحديث ملف data.json الموسوعي بالكامل خلال {elapsed} ثانية!")
    print("=" * 60)

if __name__ == "__main__":
    build_master_payload()
