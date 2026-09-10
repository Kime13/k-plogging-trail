---
name: course-data-expert
description: K-Plogging Trail 코스 데이터 추가·수정 전문가 스킬. 새 지역 또는 코스 추가 시 데이터 스키마 일관성을 보장한다.
---

# Course Data Expert

## 트리거

- 새 코스 데이터 추가 요청
- 기존 코스 좌표·하이라이트 수정
- 새 지역(도시) 추가 요청

## 코스 데이터 스키마

모든 코스 데이터는 아래 스키마를 **반드시** 따라야 한다:

```python
{
    "id": str | int,              # 고유 식별자 (지역_번호 형식)
    "name": str,                  # 한글 코스명
    "name_en": str,               # 영문 코스명
    "start": str,                 # 한글 시작점
    "end": str,                   # 한글 종점
    "start_en": str,              # 영문 시작점
    "end_en": str,                # 영문 종점
    "distance_km": float,         # 거리 (km)
    "difficulty": str,            # "Easy" | "Moderate" | "Challenge" 중 하나
    "duration_hours": float,      # 소요 시간 (시간 단위)
    "lat": float,                 # 시작점 위도
    "lon": float,                 # 시작점 경도
    "theme": str,                 # 테마 키 (THEMES 딕셔너리의 키와 일치)
    "highlights_en": list[str],   # 주요 명소 영문명 — 최대 3개
    "description_en": str,        # 영문 설명 2-3문장
    "pet_friendly": bool,         # 반려동물 동반 가능
    "plogging_tip": str,          # 플로깅 팁 (영문)
    "official_map_url": str,      # 공식 지도 URL
    "kakao_map_url": str,         # 카카오맵 URL
}
```

## 필수 체크리스트

### 코스 추가 시

1. [ ] `highlights_en` 의 각 항목이 `HIGHLIGHT_COORDS` 딕셔너리에 키로 존재하는가?
2. [ ] `difficulty` 값이 `"Easy"`, `"Moderate"`, `"Challenge"` 중 하나인가?
3. [ ] `theme` 값이 해당 지역 `THEMES` 딕셔너리의 키에 포함되는가?
4. [ ] `lat`, `lon` 좌표가 실제 시작점 위치와 일치하는가?
5. [ ] `official_map_url`, `kakao_map_url`이 유효한 URL인가?

### 새 지역 추가 시

1. [ ] `utils/{region}_courses.py` 파일에 3개 변수 export:
   - `{REGION}_COURSES` — 코스 리스트
   - `{REGION}_HIGHLIGHT_COORDS` — 하이라이트 좌표 딕셔너리
   - `{REGION}_THEMES` — 테마 딕셔너리
2. [ ] `pages/1_🗺️_Course_Finder.py`의 `REGION_DATA` 딕셔너리에 추가
3. [ ] `pages/2_♻️_Impact_Dashboard.py`의 `all_courses` 리스트에 import 추가

## 좌표 확인 방법

```python
# utils/kakao_coords.py 스크립트로 확인 가능
python -c "from utils.kakao_coords import get_coords; print(get_coords('해운대해수욕장', '부산'))"
```

## 주의 사항

- `highlights_en` 에 존재하지 않는 좌표가 있으면 지도에 마커가 누락됨
- 테마 키에 없는 값을 사용하면 Course Finder에서 해당 코스가 필터링 불가
- `id` 는 전체 코스에서 유일해야 하며 Streamlit 버튼 키로 사용됨
