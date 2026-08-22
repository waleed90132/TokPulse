import json
import random
import uuid
from datetime import datetime

# قاعدة بيانات نخبوية وصافية 100% بدون أي تكرار وبطابع عربي وخليجي بحت
arabic_trends_pool = [
    # --- قسم الصوتيات الخليجية والفخامة ---
    {"title": "شيلة العز والفخامة (ترند صاعد) 🦅", "author": "VIP Music Arabia", "category": "خليجي / فخامة", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "query": "شيلة فخامة ترند"},
    {"title": "إيقاع العود الملكي الهادئ 🎸", "author": "Oud Master KSA", "category": "خليجي / روقان", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "query": "عود هادئ ترند"},
    {"title": "موسيقى القصور والفلل الفاخرة 🏰", "author": "Luxury Beats KW", "category": "خليجي / عقارات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "query": "ديكورات فخمة ترند"},
    {"title": "صوتيات المجالس والدواوين ☕", "author": "Diwaniya Vibes", "category": "خليجي / مجلس", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "query": "سوالف ديوانية ترند"},
    {"title": "إيقاع الكشتات والبر والسفر 🏕️", "author": "Desert Chill", "category": "خليجي / فلوق", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "query": "كشتة البر ترند"},

    # --- قسم الديكور والتشطيب (مجال هندسة الديكور) ---
    {"title": "ترند تحويل المكان 180 درجة 🛠️", "author": "Makeover Pro", "category": "ديكور / تشطيب", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "query": "قبل وبعد الديكور"},
    {"title": "موسيقى استعراض الرندر والـ 3D 🎨", "author": "Render Studio", "category": "تصميم / 3D", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3", "query": "تصميم داخلي 3D"},
    {"title": "ترند بديل الخشب والرخام الحديث 🪵", "author": "Interior Vibe", "category": "ديكور / خامات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", "query": "بديل الخشب والرخام"},
    {"title": "إيقاع إضاءات النيون المخفية 💡", "author": "Lighting Design", "category": "ديكور / إضاءة", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3", "query": "إضاءة مخفية ديكور"},

    # --- قسم البودكاست والشروحات والتعليق الصوتي ---
    {"title": "موسيقى البودكاست العميقة والتحليلية 🎙️", "author": "Deep Talks AR", "category": "بودكاست / شروحات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3", "query": "بودكاست عربي ترند"},
    {"title": "إيقاع لوفاي التركيز (هادئ جداً) 📚", "author": "Study Lofi Mena", "category": "بودكاست / تركيز", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3", "query": "موسيقى لوفاي هادئة"},
    {"title": "صوتيات سرد القصص والغموض 📜", "author": "History & Mystery", "category": "بودكاست / قصص", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3", "query": "قصص واقعية ترند"},
    {"title": "نغمة أسرار علم النفس وتطوير الذات 🧠", "author": "Mind Talks", "category": "بودكاست / تطوير", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3", "query": "تطوير الذات ترند"},

    # --- قسم التجارة والدروب شيبينغ والمتاجر ---
    {"title": "موسيقى إعلانات التجارة والفلوس 💰", "author": "Business Vibes", "category": "تجارة / بزنس", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3", "query": "تجارة إلكترونية ترند"},
    {"title": "ترند تغليف الطلبات الشحن (ASMR) 📦", "author": "Packing ASMR", "category": "تجارة / متاجر", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3", "query": "تغليف طلبات متجر"},
    {"title": "إيقاع التسويق الرقمي والمبيعات 📈", "author": "Market Pro", "category": "تسويق / إعلانات", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3", "query": "تسويق رقمي ترند"},
    {"title": "صوتيات افتتاح المشاريع والمحلات ✂️", "author": "Startup AR", "category": "تجارة / افتتاح", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "query": "مشروع جديد ترند"},

    # --- قسم التحديات والكوميديا والرياكشن ---
    {"title": "إيقاع التحديات السريعة المشتعلة 🔥", "author": "Trend Maker", "category": "تحديات / رياضة", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "query": "تحديات تيك توك ترند"},
    {"title": "ترند الضحك والميمز اليومي 😂", "author": "Comedy Arabia", "category": "كوميديا / ميمز", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "query": "مضحك جدا ترند"},
    {"title": "إيقاع الرياكشنات والمواقف المحرجة 🤪", "author": "Reaction Pro", "category": "كوميديا / رياكشن", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "query": "رياكشن ترند"},

    # --- قسم التقنية والذكاء الاصطناعي ---
    {"title": "موسيقى شروحات التطبيقات والتقنية 💻", "author": "Tech Sounds AR", "category": "برمجة / تقنية", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "query": "تقنية وتطبيقات ترند"},
    {"title": "إيقاع مستقبل الذكاء الاصطناعي 🤖", "author": "AI Future", "category": "ذكاء اصطناعي / AI", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "query": "ذكاء اصطناعي ترند"},

    # --- قسم الفلوقات والروقان والحياة اليومية ---
    {"title": "أجواء الكافيهات وروقان الصباح ☕", "author": "Chill Arabia", "category": "فلوق / روقان", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3", "query": "رواق صباحي ترند"},
    {"title": "ترند السفر والمغامرات ورحلات الطيران ✈️", "author": "Travel Vibes", "category": "سفر / فلوق", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", "query": "سفر ومغامرات ترند"},
    {"title": "موسيقى الطبخ ووصفات المطبخ 🍳", "author": "Chef Beats AR", "category": "فلوق / طبخ", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3", "query": "طبخ ووصفات ترند"},

    # --- قسم التحفيز والنجاح ---
    {"title": "موسيقى التحفيز وإشعال الطاقة ⚡", "author": "Motivation Mena", "category": "تحفيز / تطوير", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3", "query": "تحفيز طاقة ترند"},
    {"title": "إيقاع النجاح وإنجاز الأهداف 🏆", "author": "Success Beats", "category": "تحفيز / نجاح", "preview": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3", "query": "نجاح وإنجاز ترند"}
]

def generate_daily_trends():
    # توليد 30 ترند متنوع وصافي (بدون تكرار)
    sample_size = min(30, len(arabic_trends_pool))
    selected_trends = random.sample(arabic_trends_pool, sample_size)
    
    final_sounds = []
    
    for trend in selected_trends:
        uses_count = round(random.uniform(12.5, 890.0), 1)
        growth_rate = random.randint(300, 1400)
        is_fire = growth_rate > 700
        fire_emoji = "🔥" if is_fire else "📈"
        
        # إنشاء رابط بحث مباشر داخل تيك توك للصوت أو الكلمة المفتاحية
        encoded_query = trend["query"].replace(" ", "%20")
        tiktok_search_url = f"https://www.tiktok.com/search?q={encoded_query}"
        
        sound_obj = {
            "id": str(uuid.uuid4())[:8],
            "title": trend["title"],
            "author": trend["author"],
            "usesCount": f"+{uses_count}K استخدام",
            "growthRate": f"{fire_emoji} نمو +{growth_rate}% اليوم",
            "previewAudioUrl": trend["preview"],
            "officialUrl": tiktok_search_url,
            "category": trend["category"]
        }
        final_sounds.append(sound_obj)
        
    data = {"sounds": final_sounds, "lastUpdated": str(datetime.now())}
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"تم توليد {len(final_sounds)} ترند عربي نخبوي بنجاح! 🚀")

if __name__ == "__main__":
    generate_daily_trends()
