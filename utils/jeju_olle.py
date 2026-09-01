HIGHLIGHT_COORDS = {
    # 올레 1코스
    "Seongsan Ilchulbong": [33.4591, 126.9405],
    "Gwangchigi Beach": [33.4525, 126.9242],
    "Siheung Coastal Road": [33.4796, 126.8954],

    # 올레 1-1코스 (우도)
    "Udo Peak": [33.5000, 126.9674],
    "Coral Beach": [33.5024, 126.9430],
    "Hagosudong Beach": [33.5142, 126.9576],

    # 올레 6코스
    "Oedolgae Rock": [33.2390, 126.5449],
    "Hwanguji Coast": [33.2419, 126.5507],
    "Beophan Port": [33.2373, 126.5156],

    # 올레 9코스
    "Hwasun Gold Sand Beach": [33.2400, 126.3336],
    "Sanbangsan Viewpoint": [33.2416, 126.3134],

    # 올레 14코스
    "Hallim Park": [33.3902, 126.2397],
    "Hyeopjae Beach": [33.3943, 126.2397],
    "Biyangdo Island View": [33.4103, 126.2273],

    # 올레 21코스
    "Jimibong Peak": [33.4993, 126.9024],
    "Jongdal Coast": [33.4619, 126.9386],
    "Udo Island View": [33.5142, 126.9576],
}

JEJU_OLLE_COURSES = [
    {
        "id": 1, "name": "올레 1코스", "name_en": "Olle Route 1 ⭐ Best",
        "start": "시흥초등학교", "end": "광치기해변",
        "start_en": "Siheung Elementary School", "end_en": "Gwangchigi Beach",
        "distance_km": 15.1, "difficulty": "Moderate", "duration_hours": 4,
        "lat": 33.4796, "lon": 126.8954,
        "theme": "coastal",
        "highlights_en": ["Seongsan Ilchulbong", "Gwangchigi Beach", "Siheung Coastal Road"],
        "description_en": "Start your Jeju plogging journey along the stunning eastern coast. This route passes by the iconic Seongsan Ilchulbong UNESCO World Heritage Site.",
        "pet_friendly": True,
        "plogging_tip": "Coastal paths collect lots of plastic waste — bring extra bags!"
    },
    {
        "id": "1-1", "name": "올레 1-1코스 (우도)", "name_en": "Olle Route 1-1 ⭐ Udo Island",
        "start": "우도 천진항", "end": "우도 천진항",
        "start_en": "Udo Cheonjin Port", "end_en": "Udo Cheonjin Port",
        "distance_km": 11.3, "difficulty": "Easy", "duration_hours": 3,
        "lat": 33.4923, "lon": 126.9502,
        "theme": "island",
        "highlights_en": ["Udo Peak", "Coral Beach", "Hagosudong Beach"],
        "description_en": "Explore the charming Udo Island on this circular loop. The island's pristine beaches and unique black pebble shores make it a perfect plogging destination.",
        "pet_friendly": True,
        "plogging_tip": "Island beaches accumulate marine debris — your cleanup makes a big difference!"
    },
    {
        "id": 6, "name": "올레 6코스", "name_en": "Olle Route 6 ⭐ Oedolgae",
        "start": "쇠소깍", "end": "외돌개",
        "start_en": "Soeso-kkak", "end_en": "Oedolgae Rock",
        "distance_km": 11.0, "difficulty": "Easy", "duration_hours": 3,
        "lat": 33.2525, "lon": 126.6234,
        "theme": "coastal",
        "highlights_en": ["Hwanguji Coast", "Beophan Port", "Oedolgae Rock"],
        "description_en": "This popular route features the iconic Oedolgae sea stack and stunning southern coastal scenery. One of the most photographed sections of the entire Olle trail.",
        "pet_friendly": True,
        "plogging_tip": "Popular tourist area — coordinate with other visitors for a group plogging session!"
    },
    {
        "id": 9, "name": "올레 9코스", "name_en": "Olle Route 9 ⭐ Sanbangsan",
        "start": "대평포구", "end": "화순금모래해변",
        "start_en": "Daepyeong Port", "end_en": "Hwasun Gold Sand Beach",
        "distance_km": 8.4, "difficulty": "Easy", "duration_hours": 2.5,
        "lat": 33.2372, "lon": 126.3616,
        "theme": "coastal",
        "highlights_en": ["Sanbangsan Viewpoint", "Hwasun Gold Sand Beach"],
        "description_en": "A short and sweet coastal route ending at the stunning Hwasun Gold Sand Beach. Perfect for a half-day plogging session with amazing views of Sanbangsan.",
        "pet_friendly": True,
        "plogging_tip": "Sandy beaches trap microplastics — every piece you collect makes a huge difference!"
    },
    {
        "id": 14, "name": "올레 14코스", "name_en": "Olle Route 14 ⭐ Hyeopjae",
        "start": "저지오름", "end": "한림항",
        "start_en": "Jeoji Oreum", "end_en": "Hallim Port",
        "distance_km": 19.5, "difficulty": "Challenge", "duration_hours": 5.5,
        "lat": 33.3308, "lon": 126.2502,
        "theme": "coastal",
        "highlights_en": ["Hallim Park", "Hyeopjae Beach", "Biyangdo Island View"],
        "description_en": "One of Jeju's most beautiful routes, featuring the famous turquoise waters of Hyeopjae Beach and views of the volcanic Biyangdo Island on the horizon.",
        "pet_friendly": True,
        "plogging_tip": "Popular beach — coordinate a group plogging event for maximum impact!"
    },
    {
        "id": 21, "name": "올레 21코스", "name_en": "Olle Route 21 ⭐ Jimibong",
        "start": "하도리", "end": "종달리",
        "start_en": "Hado Village", "end_en": "Jongdal Village",
        "distance_km": 11.7, "difficulty": "Easy", "duration_hours": 3,
        "lat": 33.5199, "lon": 126.9009,
        "theme": "coastal",
        "highlights_en": ["Jimibong Peak", "Jongdal Coast", "Udo Island View"],
        "description_en": "Climb Jimibong for a spectacular view of Udo Island and the eastern coastline before descending to the tranquil Jongdal fishing village.",
        "pet_friendly": True,
        "plogging_tip": "Short route but high impact — this pristine coast deserves your best plogging effort!"
    },
]

def get_course_by_id(course_id):
    for course in JEJU_OLLE_COURSES:
        if str(course["id"]) == str(course_id):
            return course
    return None

def get_courses_by_theme(theme):
    return [c for c in JEJU_OLLE_COURSES if c["theme"] == theme]

def get_courses_by_difficulty(difficulty):
    return [c for c in JEJU_OLLE_COURSES if c["difficulty"] == difficulty]

def get_pet_friendly_courses():
    return [c for c in JEJU_OLLE_COURSES if c["pet_friendly"]]

JEJU_THEMES = {
    "coastal": "🌊 Coastal",
    "island": "🏝️ Island",
    "forest": "🌲 Forest",
    "rural": "🌾 Rural",
    "urban": "🏙️ Urban"
}