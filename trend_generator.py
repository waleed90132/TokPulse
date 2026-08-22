import json
import random
import uuid
from datetime import datetime

# ==========================================
# 1. مكتبات الأصوات الحقيقية لكل مزاج (Vibe)
# ==========================================

lofi_sounds = [
    "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3",
    "https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8b820a454.mp3",
    "https://cdn.pixabay.com/download/audio/2021/08/09/audio_823c92157a.mp3"
]

upbeat_sounds = [
    "https://cdn.pixabay.com/download/audio/2022/01/18/audio_d0a13f69d2.mp3",
    "https://cdn.pixabay.com/download/audio/2021/10/14/audio_349d44e54f.mp3",
    "https://cdn.pixabay.com/download/audio/2021/09/06/audio_031c26b583.mp3"
]

modern_sounds = [
    "https://cdn.pixabay.com/download/audio/2021/11/24/audio_e2694b0d06.mp3",
    "https://cdn.pixabay.com/download/audio/2022/04/27/audio_87f98c4712.mp3",
    "https://cdn.pixabay.com/download/audio/2021/12/03/audio_45d944e54f.mp3"
]

dramatic_sounds = [
    "https://cdn.pixabay.com/download/audio/2022/02/15/audio_d0a13f69d2.mp3",
    "https://cdn.pixabay.com/download/audio/2021/11/24/audio_73130d2438.mp3",
    "https://cdn.pixabay.com/download/audio/2022/05/17/audio_f50d182285.mp3"
]

comedy_sounds = [
    "https://cdn.pixabay.com/download/audio/2022/03/24/audio_924b136894.mp3",
    "https://cdn.pixabay.com/download/audio/2021/09/24/audio_031c26b583.mp3",
    "https://cdn.pixabay.com/download/audio/2022/10/14/audio_60708f0384.mp3"
]

gaming_sounds = [
    "https://cdn.pixabay.com/download/audio/2022/11/22/audio_60708f0384.mp3",
    "https://cdn.pixabay.com/download/audio/2021/08/25/audio_823c92157a.mp3"
]

cars_phonk_sounds = [
    "https://cdn.pixabay.com/download/audio/2022/10/25/audio_244a0344b5.mp3",
    "https://cdn.pixabay.com/download/audio/2022/01/18/audio_d0a13f69d2.mp3"
]

fashion_sounds = [
    "https://cdn.pixabay.com/download/audio/2021/10/05/audio_1081541097.mp3",
    "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3"
]

sports_sounds = [
    "https://cdn.pixabay.com/download/audio/2021/09/06/audio_031c26b583.mp3",
    "https://cdn.pixabay.com/download/audio/2021/10/14/audio_349d44e54f.mp3"
]

spiritual_sounds = [
    "https://cdn.pixabay.com/download/audio/2022/05/17/audio_f50d182285.mp3",
    "https://cdn.pixabay.com/download/audio/2021/11/25/audio_91b3cb0384.mp3"
]

# ==========================================
# 2. الموسوعة الشاملة: 13 قسم وكل قسم 5 ترندات
# ==========================================

arabic_trends_pool = [
    # --- 1. قسم الفخامة والخليجي ---
    {"title": "شيلة العز والفخامة (ترند صاعد) 🦅", "author": "VIP Music", "category": "خليجي / فخامة", "sound_type": "dramatic", "query": "شيلة فخامة ترند"},
    {"title": "إيقاع العود الملكي الهادئ 🎸", "author": "Oud Master", "category": "خليجي / روقان", "sound_type": "lofi", "query": "عود هادئ ترند"},
    {"title": "صوتيات المجالس والدواوين ☕", "author": "Diwaniya Vibes", "category": "خليجي / مجلس", "sound_type": "lofi", "query": "سوالف ديوانية ترند"},
    {"title": "ترند الكشتات وأجواء الشتاء 🐪", "author": "Desert Chill", "category": "خليجي / فلوق", "sound_type": "lofi", "query": "كشتة البر ترند"},
    {"title": "موسيقى الخيل العربي الأصيل 🐎", "author": "Knight AR", "category": "خليجي / فروسية", "sound_type": "dramatic", "query": "خيل عربي اصيل ترند"},

    # --- 2. قسم الديكور والتشطيب ---
    {"title": "ترند تحويل المكان 180 درجة 🛠️", "author": "Makeover Pro", "category": "ديكور / تشطيب", "sound_type": "modern", "query": "قبل وبعد الديكور"},
    {"title": "موسيقى استعراض الرندر والـ 3D 🎨", "author": "Render Studio", "category": "تصميم / 3D", "sound_type": "modern", "query": "تصميم داخلي 3D"},
    {"title": "إيقاع إضاءات النيون المخفية 💡", "author": "Lighting Design", "category": "ديكور / إضاءة", "sound_type": "modern", "query": "إضاءة مخفية ديكور"},
    {"title": "ترند تنسيق الحدائق الخارجية 🌿", "author": "Garden Pro", "category": "ديكور / حدائق", "sound_type": "lofi", "query": "تنسيق حدائق ترند"},
    {"title": "صوتيات اختيار بديل الرخام والخشب 🪨", "author": "Wood & Marble", "category": "ديكور / خامات", "sound_type": "modern", "query": "بديل الرخام ديكور"},

    # --- 3. قسم البودكاست والشروحات ---
    {"title": "موسيقى البودكاست العميقة والتحليلية 🎙️", "author": "Deep Talks", "category": "بودكاست / شروحات", "sound_type": "lofi", "query": "بودكاست عربي ترند"},
    {"title": "صوتيات سرد القصص والغموض 📜", "author": "History AR", "category": "بودكاست / قصص", "sound_type": "dramatic", "query": "قصص واقعية ترند"},
    {"title": "ترند أسرار علم النفس ولغة الجسد 👁️", "author": "Mind Secrets", "category": "بودكاست / تطوير", "sound_type": "lofi", "query": "علم نفس ولغة جسد"},
    {"title": "إيقاع الشروحات التعليمية الهادئ 📚", "author": "Study Flow", "category": "بودكاست / تعليم", "sound_type": "lofi", "query": "شروحات تعليمية ترند"},
    {"title": "موسيقى قضايا الرأي العام والترند ⚖️", "author": "Public Eye", "category": "بودكاست / قضايا", "sound_type": "dramatic", "query": "قضية راي عام ترند"},

    # --- 4. قسم التجارة والبزنس ---
    {"title": "موسيقى إعلانات التجارة والفلوس 💰", "author": "Business Vibes", "category": "تجارة / بزنس", "sound_type": "upbeat", "query": "تجارة إلكترونية ترند"},
    {"title": "ترند تغليف الطلبات الشحن (ASMR) 📦", "author": "Packing ASMR", "category": "تجارة / متاجر", "sound_type": "lofi", "query": "تغليف طلبات متجر"},
    {"title": "إيقاع افتتاح المشاريع الجديدة ✂️", "author": "Startup AR", "category": "تجارة / افتتاح", "sound_type": "upbeat", "query": "افتتاح مشروع جديد"},
    {"title": "موسيقى عروض الخصومات النارية 🔥", "author": "Promo King", "category": "تسويق / عروض", "sound_type": "upbeat", "query": "عروض وخصومات ترند"},
    {"title": "ترند قصص نجاح رواد الأعمال 🚀", "author": "Success Story", "category": "تجارة / تحفيز", "sound_type": "dramatic", "query": "قصة نجاح بزنس"},

    # --- 5. قسم الكوميديا والميمز ---
    {"title": "ترند الضحك والميمز اليومي 😂", "author": "Comedy AR", "category": "كوميديا / ميمز", "sound_type": "comedy", "query": "مضحك جدا ترند"},
    {"title": "إيقاع الرياكشنات والمواقف المحرجة 🤪", "author": "Reaction Pro", "category": "كوميديا / رياكشن", "sound_type": "comedy", "query": "رياكشن ترند"},
    {"title": "صوتيات المقالب بين الأصحاب 🤡", "author": "Prankster", "category": "كوميديا / مقالب", "sound_type": "comedy", "query": "مقلب بالاصحاب ترند"},
    {"title": "ترند فصلات آخر الليل 🌚", "author": "Night Laughs", "category": "كوميديا / يوميات", "sound_type": "comedy", "query": "فصلات اخر الليل"},
    {"title": "موسيقى تقليد المشاهير الساخرة 🎭", "author": "Imitator AR", "category": "كوميديا / ساخر", "sound_type": "comedy", "query": "تقليد مشاهير ترند"},

    # --- 6. قسم التقنية والـ AI ---
    {"title": "موسيقى شروحات التطبيقات والتقنية 💻", "author": "Tech Sounds", "category": "برمجة / تقنية", "sound_type": "modern", "query": "تقنية وتطبيقات ترند"},
    {"title": "إيقاع مستقبل الذكاء الاصطناعي 🤖", "author": "AI Future", "category": "تقنية / AI", "sound_type": "modern", "query": "ذكاء اصطناعي ترند"},
    {"title": "ترند فتح صناديق الأجهزة (Unboxing) 📦", "author": "Tech Unbox", "category": "تقنية / مراجعات", "sound_type": "modern", "query": "مراجعة اجهزة ترند"},
    {"title": "صوتيات حيل واسرار الايفون 📱", "author": "Apple Hacks", "category": "تقنية / اسرار", "sound_type": "modern", "query": "اسرار الايفون ترند"},
    {"title": "موسيقى تجميعات البي سي (PC Build) 🖥️", "author": "PC Builder", "category": "تقنية / هاردوير", "sound_type": "modern", "query": "تجميعة بي سي ترند"},

    # --- 7. قسم الفلوقات والطبخ ---
    {"title": "أجواء الكافيهات وروقان الصباح ☕", "author": "Chill Arabia", "category": "فلوق / روقان", "sound_type": "lofi", "query": "رواق صباحي ترند"},
    {"title": "موسيقى الطبخ ووصفات المطبخ 🍳", "author": "Chef Beats", "category": "فلوق / طبخ", "sound_type": "upbeat", "query": "طبخ ووصفات ترند"},
    {"title": "ترند السفر ورحلات الطيران ✈️", "author": "Travel Vibes", "category": "فلوق / سفر", "sound_type": "lofi", "query": "سفر ومغامرات ترند"},
    {"title": "صوتيات يوميات الموظفين 💼", "author": "Office Life", "category": "فلوق / يوميات", "sound_type": "lofi", "query": "يوميات موظف ترند"},
    {"title": "إيقاع روتين المساء والعناية 🌙", "author": "Night Routine", "category": "فلوق / عناية", "sound_type": "lofi", "query": "روتين المساء ترند"},

    # --- 8. قسم التحفيز والنجاح ---
    {"title": "موسيقى التحفيز وإشعال الطاقة ⚡", "author": "Motivation Mena", "category": "تحفيز / تطوير", "sound_type": "upbeat", "query": "تحفيز طاقة ترند"},
    {"title": "إيقاع النجاح وإنجاز الأهداف 🏆", "author": "Goal Hunter", "category": "تحفيز / نجاح", "sound_type": "upbeat", "query": "تحفيز نجاح ترند"},
    {"title": "ترند التغلب على الصعاب 💪", "author": "Never Give Up", "category": "تحفيز / قوة", "sound_type": "dramatic", "query": "ارادة وقوة ترند"},
    {"title": "صوتيات الاستيقاظ المبكر والإنتاجية 🌅", "author": "Morning Power", "category": "تحفيز / انتاجية", "sound_type": "lofi", "query": "استيقاظ مبكر ترند"},
    {"title": "موسيقى خطابات ملهمة وعميقة 🗣️", "author": "Deep Speech", "category": "تحفيز / خطابات", "sound_type": "dramatic", "query": "خطاب ملهم ترند"},

    # --- 9. قسم الجيمنج والألعاب 🎮 ---
    {"title": "ترند لقطات الجيمنج والكلتشات 🎮", "author": "Gamer Pro", "category": "العاب / جيمنج", "sound_type": "gaming", "query": "لقطات جيمنج ترند"},
    {"title": "إيقاع تفتيح البكجات والحظ 🎁", "author": "Loot Box", "category": "العاب / حظ", "sound_type": "upbeat", "query": "تفتيح بكجات ترند"},
    {"title": "موسيقى ألعاب الرعب والغموض 🧟‍♂️", "author": "Scary Plays", "category": "العاب / رعب", "sound_type": "dramatic", "query": "العاب رعب ترند"},
    {"title": "صوتيات تحديات فيفا وجلادتها ⚽", "author": "Fifa King", "category": "العاب / فيفا", "sound_type": "gaming", "query": "تحديات فيفا ترند"},
    {"title": "ترند احتراف العاب الشوتر 🎯", "author": "Aim Bot", "category": "العاب / شوتر", "sound_type": "gaming", "query": "العاب شوتر ترند"},

    # --- 10. قسم السيارات والمحركات 🏎️ ---
    {"title": "ترند السيارات المعدلة واستعراضها 🏎️", "author": "Auto Show", "category": "سيارات / تعديل", "sound_type": "cars", "query": "سيارات معدلة ترند"},
    {"title": "إيقاع الدريفت والتفحيط الحماسي 💨", "author": "Drift King", "category": "سيارات / دريفت", "sound_type": "cars", "query": "دريفت سيارات ترند"},
    {"title": "موسيقى استعراض الفخامة والسيارات 🚙", "author": "VIP Garage", "category": "سيارات / فخامة", "sound_type": "modern", "query": "سيارات فخمة ترند"},
    {"title": "صوتيات غسيل السيارات (ديتيلنج) 🧽", "author": "Car Wash ASMR", "category": "سيارات / تنظيف", "sound_type": "lofi", "query": "غسيل سيارات ترند"},
    {"title": "ترند تجمعات السيارات الرياضية 🏁", "author": "Car Meet", "category": "سيارات / تجمعات", "sound_type": "cars", "query": "تجمع سيارات ترند"},

    # --- 11. قسم الرياضة والجيم 🏋️ ---
    {"title": "ترند الجيم وبناء العضلات 🏋️", "author": "Gym Beast", "category": "رياضة / جيم", "sound_type": "sports", "query": "تمارين جيم ترند"},
    {"title": "إيقاع كرة القدم والأهداف ⚽", "author": "Goal Strike", "category": "رياضة / كرة قدم", "sound_type": "sports", "query": "مهارات كرة قدم ترند"},
    {"title": "موسيقى التحديات الرياضية الصعبة 🥊", "author": "Fighter AR", "category": "رياضة / تحديات", "sound_type": "sports", "query": "تحدي رياضي ترند"},
    {"title": "صوتيات رياضة البادل والتنس 🎾", "author": "Padel Smash", "category": "رياضة / بادل", "sound_type": "upbeat", "query": "رياضة بادل ترند"},
    {"title": "ترند تمارين الكارديو والحرق 🏃‍♂️", "author": "Cardio Burn", "category": "رياضة / لياقة", "sound_type": "sports", "query": "تمارين كارديو ترند"},

    # --- 12. قسم الموضة والجمال 👗 ---
    {"title": "ترند الموضة وتنسيق الأزياء 👗", "author": "Fashion Walk", "category": "موضة / ستايل", "sound_type": "fashion", "query": "تنسيق ملابس ترند"},
    {"title": "موسيقى الميك أب وتجهيز العرايس 👰", "author": "Beauty Glow", "category": "موضة / ميك_اب", "sound_type": "fashion", "query": "ميك اب ترند"},
    {"title": "إيقاع استعراض العطور الفاخرة ✨", "author": "Perfume AR", "category": "موضة / عطور", "sound_type": "lofi", "query": "عطور فخمة ترند"},
    {"title": "صوتيات العناية بالبشرة (Skin Care) 🧴", "author": "Clear Skin", "category": "موضة / عناية", "sound_type": "lofi", "query": "عناية بالبشرة ترند"},
    {"title": "ترند تسريحات الشعر والميكوفور 💇‍♀️", "author": "Hair Style Pro", "category": "موضة / شعر", "sound_type": "fashion", "query": "تسريحات شعر ترند"},

    # --- 13. قسم الصحة النفسية والروحانيات 🧘 ---
    {"title": "صوتيات الراحة النفسية والهدوء 🧘", "author": "Mind Peace", "category": "تطوير / راحة", "sound_type": "spiritual", "query": "راحة نفسية ترند"},
    {"title": "إيقاع التأمل واليوغا 🌿", "author": "Zen Arabia", "category": "تطوير / تأمل", "sound_type": "spiritual", "query": "موسيقى هادئة للتأمل"},
    {"title": "ترند الاقتباسات العميقة والمؤثرة 🕯️", "author": "Deep Quotes", "category": "تطوير / اقتباسات", "sound_type": "dramatic", "query": "اقتباسات عميقة ترند"},
    {"title": "موسيقى التخلص من التوتر والقلق 🍃", "author": "Anxiety Relief", "category": "تطوير / هدوء", "sound_type": "lofi", "query": "التخلص من التوتر"},
    {"title": "صوتيات التأكيدات الإيجابية الصباحية 🌞", "author": "Morning Vibes", "category": "تطوير / ايجابية", "sound_type": "spiritual", "query": "طاقة ايجابية ترند"}
]

def get_preview_url(sound_type):
    if sound_type == "lofi": return random.choice(lofi_sounds)
    elif sound_type == "upbeat": return random.choice(upbeat_sounds)
    elif sound_type == "modern": return random.choice(modern_sounds)
    elif sound_type == "dramatic": return random.choice(dramatic_sounds)
    elif sound_type == "comedy": return random.choice(comedy_sounds)
    elif sound_type == "gaming": return random.choice(gaming_sounds)
    elif sound_type == "cars": return random.choice(cars_phonk_sounds)
    elif sound_type == "fashion": return random.choice(fashion_sounds)
    elif sound_type == "sports": return random.choice(sports_sounds)
    elif sound_type == "spiritual": return random.choice(spiritual_sounds)
    else: return random.choice(modern_sounds)

def generate_daily_trends():
    # سحب 50 ترند بشكل عشوائي من الـ 65 ترند المتاحة
    sample_size = min(50, len(arabic_trends_pool))
    selected_trends = random.sample(arabic_trends_pool, sample_size)
    
    final_sounds = []
    
    for trend in selected_trends:
        uses_count = round(random.uniform(15.0, 990.0), 1)
        growth_rate = random.randint(300, 1500)
        is_fire = growth_rate > 700
        fire_emoji = "🔥" if is_fire else "📈"
        
        encoded_query = trend["query"].replace(" ", "%20")
        tiktok_search_url = f"https://www.tiktok.com/search?q={encoded_query}"
        preview_url = get_preview_url(trend["sound_type"])
        
        sound_obj = {
            "id": str(uuid.uuid4())[:8],
            "title": trend["title"],
            "author": trend["author"],
            "usesCount": f"+{uses_count}K استخدام",
            "growthRate": f"{fire_emoji} نمو +{growth_rate}% اليوم",
            "previewAudioUrl": preview_url,
            "officialUrl": tiktok_search_url,
            "category": trend["category"]
        }
        final_sounds.append(sound_obj)
        
    data = {"sounds": final_sounds, "lastUpdated": str(datetime.now())}
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"تم توليد {len(final_sounds)} ترند لـ 13 قسم بأصوات واقعية بنجاح! 🚀")

if __name__ == "__main__":
    generate_daily_trends()
