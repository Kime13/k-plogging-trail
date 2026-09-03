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
    "Hwanguji Coast": [33.2419, 126.5507],
    "Beophan Port": [33.2373, 126.5156],
    "Oedolgae Rock": [33.2390, 126.5449],
    # 올레 10코스
    "Hwasun Gold Sand Beach": [33.2400, 126.3336],
    "Sanbangsan Mountain": [33.2416, 126.3134],
    "Songaksan Mountain": [33.1991, 126.2898],
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
        "plogging_tip": "Coastal paths collect lots of plastic waste — bring extra bags!",
        "official_map_url": "https://www.jejuolle.org/trail#/road/01",
        "kakao_map_url": "https://map.kakao.com/?urlX=478193.99999999785&urlY=-4168.000000000466&urlLevel=3&itemId=10626234&q=%EC%98%AC%EB%A0%88%EA%B8%B8%201%EC%BD%94%EC%8A%A4(%EC%8B%9C%ED%9D%A5-%EA%B4%91%EC%B9%98%EA%B8%B0%20%EC%98%AC%EB%A0%88)&srcid=10626234&map_type=TYPE_MAP",
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
        "plogging_tip": "Island beaches accumulate marine debris — your cleanup makes a big difference!",
        "official_map_url": "https://www.jejuolle.org/trail#/road/01-1",
        "kakao_map_url": "https://map.kakao.com/?urlX=490587.99999999825&urlY=5095.000000002328&urlLevel=3&itemId=12753592&q=%EC%98%AC%EB%A0%88%EA%B8%B8%201-1%EC%BD%94%EC%8A%A4(%EC%9A%B0%EB%8F%84-%EC%98%AC%EB%A0%88)&srcid=12753592&map_type=TYPE_MAP",
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
        "plogging_tip": "Popular tourist area — coordinate with other visitors for a group plogging session!",
        "official_map_url": "https://www.jejuolle.org/trail#/road/06",
        "kakao_map_url": "https://map.kakao.com/?urlX=402570.0000000021&urlY=-69085&urlLevel=3&itemId=8015963&q=%EC%98%AC%EB%A0%88%EA%B8%B8%206%EC%BD%94%EC%8A%A4(%EC%87%A0%EC%86%8C%EA%B9%8D-%EC%84%9C%EA%B7%80%ED%8F%AC%20%EC%98%AC%EB%A0%88)&srcid=8015963&map_type=TYPE_MAP",
    },
    {
        "id": 10, "name": "올레 10코스", "name_en": "Olle Route 10 ⭐ Sanbangsan",
        "start": "화순금모래해변", "end": "모슬포항",
        "start_en": "Hwasun Gold Sand Beach", "end_en": "Moseulpo Port",
        "distance_km": 15.5, "difficulty": "Moderate", "duration_hours": 4,
        "lat": 33.2400, "lon": 126.3336,
        "theme": "coastal",
        "highlights_en": ["Hwasun Gold Sand Beach", "Sanbangsan Mountain", "Songaksan Mountain"],
        "description_en": "Walk past the iconic Sanbangsan volcanic dome and the dramatic Songaksan crater overlooking Marado Island. This scenic coastal route captures the wild beauty of Jeju's southwestern tip.",
        "pet_friendly": True,
        "plogging_tip": "Sandy beaches and volcanic coastal paths — bring extra bags for marine debris!",
        "official_map_url": "https://www.jejuolle.org/trail#/road/10",
        "kakao_map_url": ""kakao_map_url": "https://map.kakao.com/?urlX=334711.0000000014&urlY=-79995.99999999977&urlLevel=3&itemId=12753435&q=%EC%98%AC%EB%A0%88%EA%B8%B8%2010%EC%BD%94%EC%8A%A4(%ED%99%94%EC%88%9C-%EB%AA%A8%EC%8A%AC%ED%8F%AC%20%EC%98%AC%EB%A0%88)&srcid=12753435&map_type=TYPE_MAP",
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
        "plogging_tip": "Popular beach — coordinate a group plogging event for maximum impact!",
        "official_map_url": "https://www.jejuolle.org/trail#/road/14",
        "kakao_map_url": "https://map.kakao.com/?urlX=320310.00000000163&urlY=-28236.999999999534&urlLevel=3&itemId=12753448&q=%EC%98%AC%EB%A0%88%EA%B8%B8%2014%EC%BD%94%EC%8A%A4(%EC%A0%80%EC%A7%80-%ED%95%9C%EB%A6%BC%20%EC%98%AC%EB%A0%88)&srcid=12753448&map_type=TYPE_MAP",
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
        "plogging_tip": "Short route but high impact — this pristine coast deserves your best plogging effort!",
        "official_map_url": "https://www.jejuolle.org/trail#/road/21",
        "kakao_map_url": "https://map.kakao.com/?urlX=476981.9999999975&urlY=7301.99999999837&urlLevel=3&itemId=18502107&q=%EC%98%AC%EB%A0%88%EA%B8%B8%2021%EC%BD%94%EC%8A%A4&srcid=18502107&map_type=TYPE_MAP",
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