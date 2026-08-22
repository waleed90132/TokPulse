import json
import random
import uuid
from datetime import datetime

# قاعدة بيانات ضخمة (65 ترند متنوع وشامل)
arabic_trends_pool = [
    # --- قسم الصوتيات الخليجية والفخامة ---
    {"title": "ترند الهيبة والفخامة 🦅", "author": "VIP Music", "category": "خليجي / فخامة", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "url": "https://www.tiktok.com/tag/فخامة"},
    {"title": "شيلة العز والفخر 🐎", "author": "Arabian Beats", "category": "خليجي / شيلات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "url": "https://www.tiktok.com/tag/شيلات"},
    {"title": "إيقاع العود الحديث 🎸", "author": "Oud Master", "category": "خليجي / روقان", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "url": "https://www.tiktok.com/tag/عود"},
    {"title": "موسيقى القصور والفلل 🏰", "author": "Luxury Sounds", "category": "خليجي / عقارات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "url": "https://www.tiktok.com/tag/عقارات"},
    {"title": "ترند المجالس والدواوين ☕", "author": "Diwaniya Vibes", "category": "خليجي / ديكور", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "url": "https://www.tiktok.com/tag/مجلس"},
    {"title": "إيقاع الكشتات والبر 🏕️", "author": "Desert Beats", "category": "خليجي / فلوق", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "url": "https://www.tiktok.com/tag/كشتة"},
    {"title": "موسيقى الزفات والمناسبات 🎉", "author": "Wedding AR", "category": "خليجي / أفراح", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3", "url": "https://www.tiktok.com/tag/زفة"},
    {"title": "صوتيات الخيل والفروسية 🏇", "author": "Knight Vibes", "category": "خليجي / فروسية", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", "url": "https://www.tiktok.com/tag/خيل"},
    
    # --- قسم البودكاست والشروحات ---
    {"title": "موسيقى البودكاست العميقة 🎙️", "author": "Deep Talks", "category": "بودكاست / شروحات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3", "url": "https://www.tiktok.com/tag/بودكاست"},
    {"title": "إيقاع التركيز والدراسة 📚", "author": "Study Lofi", "category": "بودكاست / تركيز", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3", "url": "https://www.tiktok.com/tag/لوفاي"},
    {"title": "موسيقى الشروحات الهادئة 📝", "author": "Tech Whisper", "category": "بودكاست / تعليم", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3", "url": "https://www.tiktok.com/tag/تعليم"},
    {"title": "صوتيات القصص التاريخية 📜", "author": "History AR", "category": "بودكاست / قصص", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3", "url": "https://www.tiktok.com/tag/تاريخ"},
    {"title": "إيقاع التحليل والنقد 🔍", "author": "Review Master", "category": "بودكاست / تقييم", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3", "url": "https://www.tiktok.com/tag/مراجعة"},
    {"title": "نغمة أسرار علم النفس 🧠", "author": "Mind Talks", "category": "بودكاست / تطوير", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3", "url": "https://www.tiktok.com/tag/علم_نفس"},

    # --- قسم التجارة والبزنس ---
    {"title": "ترند التجارة والفلوس 💰", "author": "Business Vibes", "category": "تجارة / بزنس", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3", "url": "https://www.tiktok.com/tag/بزنس"},
    {"title": "موسيقى الدروب شيبينغ 📦", "author": "Ecom AR", "category": "تجارة / منتجات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3", "url": "https://www.tiktok.com/tag/دروب_شيبينج"},
    {"title": "إيقاع التسويق والمبيعات 📈", "author": "Market Pro", "category": "تسويق / إعلانات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "url": "https://www.tiktok.com/tag/تسويق"},
    {"title": "ترند التغليف والشحن 🎁", "author": "Packing ASMR", "category": "تجارة / متاجر", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "url": "https://www.tiktok.com/tag/تغليف_طلبات"},
    {"title": "صوتيات إعلانات المطاعم 🍔", "author": "Foodie Beats", "category": "تسويق / مطاعم", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "url": "https://www.tiktok.com/tag/مطاعم"},
    {"title": "إيقاع افتتاح المشاريع ✂️", "author": "Startup AR", "category": "تجارة / افتتاح", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "url": "https://www.tiktok.com/tag/مشروع_جديد"},
    {"title": "ترند العروض والخصومات 🏷️", "author": "Promo King", "category": "تسويق / عروض", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "url": "https://www.tiktok.com/tag/خصومات"},

    # --- قسم التحديات والميمز ---
    {"title": "إيقاع التحديات السريع 🔥", "author": "Trend Maker", "category": "تحديات / رياضة", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "url": "https://www.tiktok.com/tag/تحدي"},
    {"title": "ترند الميمز والضحك 😂", "author": "Comedy AR", "category": "كوميديا / ميمز", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3", "url": "https://www.tiktok.com/tag/ضحك"},
    {"title": "صوتيات المقالب السريعة 🤡", "author": "Prankster", "category": "كوميديا / مقالب", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", "url": "https://www.tiktok.com/tag/مقلب"},
    {"title": "إيقاع الرياكشنات المضحكة 🤪", "author": "Reaction Pro", "category": "كوميديا / رياكشن", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3", "url": "https://www.tiktok.com/tag/رياكشن"},
    {"title": "ترند التحديات الرياضية 🏋️", "author": "Gym Motivation", "category": "تحديات / جيم", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3", "url": "https://www.tiktok.com/tag/جيم"},
    {"title": "إيقاع المواقف المحرجة 🤦‍♂️", "author": "Awkward Moments", "category": "كوميديا / يوميات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3", "url": "https://www.tiktok.com/tag/مواقف"},

    # --- قسم الديكور والتصميم والمعمار ---
    {"title": "ترند التصوير المعماري 🏢", "author": "Arch Beats", "category": "ديكور / عقارات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3", "url": "https://www.tiktok.com/tag/ديكور"},
    {"title": "إيقاع قبل وبعد التشطيب 🛠️", "author": "Makeover AR", "category": "ديكور / تشطيب", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3", "url": "https://www.tiktok.com/tag/تشطيب"},
    {"title": "موسيقى استعراض الرندر 🎨", "author": "Render Pro", "category": "تصميم / 3D", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3", "url": "https://www.tiktok.com/tag/3D"},
    {"title": "صوتيات تنسيق الأثاث 🛋️", "author": "Interior Vibe", "category": "ديكور / تأثيث", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3", "url": "https://www.tiktok.com/tag/أثاث"},
    {"title": "إيقاع بديل الرخام والخشب 🪵", "author": "Wood & Marble", "category": "ديكور / خامات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3", "url": "https://www.tiktok.com/tag/بديل_الخشب"},
    {"title": "ترند الإضاءات المخفية والنيون 💡", "author": "Lighting Studio", "category": "ديكور / إضاءة", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "url": "https://www.tiktok.com/tag/إضاءة"},
    {"title": "صوتيات تصميم الحدائق والمظلات 🌿", "author": "Garden Design", "category": "ديكور / حدائق", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "url": "https://www.tiktok.com/tag/حدائق"},

    # --- قسم التقنية والذكاء الاصطناعي ---
    {"title": "موسيقى الشروحات التقنية 💻", "author": "Tech Sounds", "category": "برمجة / تقنية", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "url": "https://www.tiktok.com/tag/تقنية"},
    {"title": "إيقاع الذكاء الاصطناعي 🤖", "author": "AI Future", "category": "ذكاء اصطناعي / AI", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "url": "https://www.tiktok.com/tag/ذكاء_اصطناعي"},
    {"title": "ترند تطبيقات الموبايل 📱", "author": "App Dev", "category": "برمجة / تطبيقات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "url": "https://www.tiktok.com/tag/تطبيقات"},
    {"title": "صوتيات الخدع المخفية 🔓", "author": "Hacker Vibe", "category": "تقنية / أسرار", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "url": "https://www.tiktok.com/tag/أسرار"},
    {"title": "إيقاع مراجعة الأجهزة 📱", "author": "Unboxing AR", "category": "تقنية / مراجعات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3", "url": "https://www.tiktok.com/tag/مراجعة"},
    {"title": "ترند التجميعات والـ PC 🖥️", "author": "PC Builder", "category": "تقنية / هاردوير", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", "url": "https://www.tiktok.com/tag/بي_سي"},

    # --- قسم الفلوقات والروقان ---
    {"title": "أجواء الكافيهات والروقان ☕", "author": "Chill Arabia", "category": "فلوق / روقان", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3", "url": "https://www.tiktok.com/tag/روقان"},
    {"title": "ترند السفر والمغامرات ✈️", "author": "Travel Vibes", "category": "سفر / فلوق", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3", "url": "https://www.tiktok.com/tag/سفر"},
    {"title": "إيقاع الصباح والقهوة 🌅", "author": "Morning Lofi", "category": "فلوق / يوميات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3", "url": "https://www.tiktok.com/tag/صباحيات"},
    {"title": "موسيقى الطبخ والوصفات 🍳", "author": "Chef Beats", "category": "فلوق / طبخ", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3", "url": "https://www.tiktok.com/tag/طبخ"},
    {"title": "صوتيات العناية والميك أب 💄", "author": "Beauty Glow", "category": "فلوق / عناية", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3", "url": "https://www.tiktok.com/tag/ميك_اب"},
    {"title": "ترند السيارات الكلاسيكية 🚙", "author": "Classic Auto", "category": "سيارات / كلاسيك", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3", "url": "https://www.tiktok.com/tag/سيارات"},

    # --- قسم التحفيز والدراما والقصص ---
    {"title": "صوتيات الدراما والغموض 🎭", "author": "Cinema AR", "category": "قصص / رعب", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3", "url": "https://www.tiktok.com/tag/قصص"},
    {"title": "موسيقى التحفيز والطاقة ⚡", "author": "Motivation AR", "category": "تحفيز / تطوير", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3", "url": "https://www.tiktok.com/tag/تحفيز"},
    {"title": "إيقاع النجاح والإنجاز 🏆", "author": "Success Beats", "category": "تحفيز / نجاح", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "url": "https://www.tiktok.com/tag/نجاح"},
    {"title": "صوتيات الحزن والمواقف 💔", "author": "Sad Strings", "category": "دراما / مواقف", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "url": "https://www.tiktok.com/tag/حزن"},
    {"title": "ترند الاقتباسات العميقة 📖", "author": "Quotes AR", "category": "تحفيز / اقتباسات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "url": "https://www.tiktok.com/tag/اقتباس"},
    {"title": "نغمة الإصرار والتحدي 🧗", "author": "Never Give Up", "category": "تحفيز / قوة", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "url": "https://www.tiktok.com/tag/إصرار"},

    # --- قسم المنوعات والجيمنج ---
    {"title": "إيقاع السيارات المعدلة 🏎️", "author": "Car Drift", "category": "سيارات / دريفت", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "url": "https://www.tiktok.com/tag/سيارات"},
    {"title": "ترند تنظيف وترتيب البيت 🧹", "author": "Clean ASMR", "category": "يوميات / تنظيف", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "url": "https://www.tiktok.com/tag/تنظيف"},
    {"title": "موسيقى تصوير المنتجات 📸", "author": "Product Shot", "category": "تصوير / منتجات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3", "url": "https://www.tiktok.com/tag/تصوير"},
    {"title": "إيقاع ألعاب الفيديو والجيمنج 🎮", "author": "Gamer Pro", "category": "العاب / جيمنج", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", "url": "https://www.tiktok.com/tag/جيمنج"},
    {"title": "ترند الملابس والموضة 👗", "author": "Fashion Walk", "category": "موضة / ستايل", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3", "url": "https://www.tiktok.com/tag/موضة"},
    {"title": "صوتيات الألغاز والذكاء 🧩", "author": "Puzzle Beats", "category": "تحديات / ذكاء", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3", "url": "https://www.tiktok.com/tag/ألغاز"}
]

def generate_daily_trends():
    # سحب 50 ترند بشكل آمن ومحمي من الأخطاء
    sample_size = min(50, len(arabic_trends_pool))
    selected_trends = random.sample(arabic_trends_pool, sample_size)
    
    final_sounds = []
    
    for trend in selected_trends:
        uses_count = round(random.uniform(5.5, 980.0), 1)
        growth_rate = random.randint(250, 1500)
        is_fire = growth_rate > 700
        fire_emoji = "🔥" if is_fire else "📈"
        
        sound_obj = {
            "id": str(uuid.uuid4())[:8],
            "title": trend["title"],
            "author": trend["author"],
            "usesCount": f"+{uses_count}K استخدام",
            "growthRate": f"{fire_emoji} نمو +{growth_rate}% اليوم",
            "previewAudioUrl": trend["preview"],
            "officialUrl": trend["url"],
            "category": trend["category"]
        }
        final_sounds.append(sound_obj)
        
    data = {"sounds": final_sounds, "lastUpdated": str(datetime.now())}
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"تم تحديث {len(final_sounds)} ترند بنجاح! 🚀")

if __name__ == "__main__":
    generate_daily_trends()
