SEOUL_COURSES = [
    {
        "id": "seoul_1",
        "name": "서울둘레길 4코스 망우·용마산",
        "name_en": "Seoul Dulegil Route 4 - Mangu & Yongmasan",
        "start": "화랑대역", "end": "깔딱고개쉼터",
        "start_en": "Hwarangdae Station Exit 1", "end_en": "Kkalddag-gogae Rest Area",
        "distance_km": 7.3, "difficulty": "Easy", "duration_hours": 3,
        "lat": 37.6198, "lon": 127.0835,
        "theme": "mountain",
        "highlights_en": ["Yongma Skywalk", "Mangu History Culture Park", "Yongmasan Mountain"],
        "description_en": "A well-maintained urban mountain trail connecting Yongmasan and Mangwusan. The newly opened Yongma Skywalk offers breathtaking 360° panoramic views of Seoul's cityscape.",
        "pet_friendly": False,
        "plogging_tip": "Mountain trails collect wind-blown litter — check both sides of the trail carefully!"
    },
    {
        "id": "seoul_2",
        "name": "서울둘레길 5코스 아차산",
        "name_en": "Seoul Dulegil Route 5 - Achasan",
        "start": "깔딱고개쉼터", "end": "광나루역",
        "start_en": "Sagajeong Station Exit 4", "end_en": "Gwangnaru Station Exit 1",
        "distance_km": 4.6, "difficulty": "Moderate", "duration_hours": 2.5,
        "lat": 37.5809, "lon": 127.0885,
        "theme": "mountain",
        "highlights_en": ["Achasan Sunrise Plaza", "Goguryeo Pavilion", "Achasan Mountain"],
        "description_en": "Walk the historic ridge of Achasan with panoramic Han River views. Rich in Goguryeo-era fortress ruins, this culturally significant 4.6km trail connects ancient history with modern Seoul.",
        "pet_friendly": False,
        "plogging_tip": "Historic fortress ruins surround the trail — keep this culturally significant site pristine!"
    },
    {
        "id": "seoul_3",
        "name": "서울둘레길 9코스 대모·구룡산",
        "name_en": "Seoul Dulegil Route 9 - Daemo & Guryongsan",
        "start": "수서역", "end": "매헌시민의숲",
        "start_en": "Suseo Station Exit 6", "end_en": "Maeheon Citizens Forest",
        "distance_km": 10.7, "difficulty": "Challenge", "duration_hours": 5,
        "lat": 37.4855, "lon": 127.1044,
        "theme": "nature",
        "highlights_en": ["Daemo Mountain Entrance", "Guryongsan Mountain", "Maeheon Citizens Forest"],
        "description_en": "A rewarding forest trail through two connected mountains in southern Seoul. End at the beautiful Maeheon Citizens Forest with its historic memorial to independence hero Yun Bong-gil.",
        "pet_friendly": True,
        "plogging_tip": "Dense forest sections hide litter under fallen leaves — bring a grabber tool!"
    },
    {
        "id": "seoul_4",
        "name": "서울둘레길 15코스 노을·하늘공원",
        "name_en": "Seoul Dulegil Route 15 - Noeul & Haneul Park",
        "start": "가양역", "end": "증산역",
        "start_en": "Gayang Station", "end_en": "Jeungsan Station",
        "distance_km": 6.2, "difficulty": "Easy", "duration_hours": 2.5,
        "lat": 37.5614, "lon": 126.8544,
        "theme": "park",
        "highlights_en": ["Noeul Park", "Haneul Park", "World Cup Park"],
        "description_en": "Walk through Seoul's iconic ecological parks built on a former landfill. The silver grass fields of Haneul Park and stunning sunset views over the Han River make this an unforgettable plogging experience.",
        "pet_friendly": True,
        "plogging_tip": "Popular weekend picnic destination — morning plogging yields the most waste after busy weekends!"
    },
]

SEOUL_HIGHLIGHT_COORDS = {
    # 4코스 망우·용마산
    "Yongma Skywalk": [37.5829, 127.1032],
    "Mangu History Culture Park": [37.5989, 127.1144],
    "Yongmasan Mountain": [37.5829, 127.1032],
    # 5코스 아차산
    "Achasan Sunrise Plaza": [37.5601, 127.1016],
    "Goguryeo Pavilion": [37.5582, 127.1022],
    "Achasan Mountain": [37.5522, 127.0896],
    # 9코스 대모·구룡산
    "Daemo Mountain Entrance": [37.4915, 127.0731],
    "Guryongsan Mountain": [37.4689, 127.0616],
    "Maeheon Citizens Forest": [37.4709, 127.0359],
    # 15코스 노을·하늘공원
    "Noeul Park": [37.5741, 126.8758],
    "Haneul Park": [37.5685, 126.8869],
    "World Cup Park": [37.5632, 126.8976],
}

SEOUL_THEMES = {
    "mountain": "⛰️ Mountain",
    "nature": "🌿 Nature",
    "park": "🌳 Park",
}