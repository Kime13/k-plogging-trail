---
name: test-driven-development
description: 코스 데이터 검증, API 연동 테스트, Streamlit 동작 확인 등 기능 구현·버그 수정 전 테스트부터 작성한다.
---

# Test-Driven Development — 테스트 먼저

**핵심:** 테스트가 실패하는 걸 보지 않았으면, 그 테스트가 올바른지 알 수 없다.

## Iron Law

```
실패하는 테스트 없이 프로덕션 코드를 작성하지 않는다.
```

## Red-Green-Refactor

```
RED   → 실패하는 테스트 작성
       ↓
      실패 확인 (pytest 실행)
       ↓
GREEN → 테스트를 통과하는 최소 코드 작성
       ↓
      전체 테스트 통과 확인
       ↓
REFACTOR → 중복 제거, 이름 개선
       ↓
      테스트 여전히 통과 확인 → 다음 RED
```

## K-Plogging Trail 테스트 유형

### 1. 코스 데이터 정합성 테스트

```python
# tests/test_course_data.py
import pytest
from utils.jeju_olle import JEJU_OLLE_COURSES, HIGHLIGHT_COORDS, JEJU_THEMES
from utils.seoul_courses import SEOUL_COURSES, SEOUL_HIGHLIGHT_COORDS, SEOUL_THEMES
from utils.busan_courses import BUSAN_COURSES, BUSAN_HIGHLIGHT_COORDS, BUSAN_THEMES

REGIONS = [
    (JEJU_OLLE_COURSES, HIGHLIGHT_COORDS, JEJU_THEMES),
    (SEOUL_COURSES, SEOUL_HIGHLIGHT_COORDS, SEOUL_THEMES),
    (BUSAN_COURSES, BUSAN_HIGHLIGHT_COORDS, BUSAN_THEMES),
]

@pytest.mark.parametrize("courses,coords,themes", REGIONS)
def test_highlights_have_coords(courses, coords, themes):
    """모든 highlights_en 항목이 HIGHLIGHT_COORDS에 존재하는가"""
    for c in courses:
        for h in c["highlights_en"]:
            assert h in coords, f"Missing coord: {h} in {c['name_en']}"

@pytest.mark.parametrize("courses,coords,themes", REGIONS)
def test_difficulty_values(courses, coords, themes):
    """difficulty가 허용값 중 하나인가"""
    for c in courses:
        assert c["difficulty"] in ("Easy", "Moderate", "Challenge"), \
            f"Bad difficulty: {c['difficulty']} in {c['name_en']}"

@pytest.mark.parametrize("courses,coords,themes", REGIONS)
def test_theme_in_themes(courses, coords, themes):
    """theme이 THEMES 딕셔너리 키에 있는가"""
    for c in courses:
        assert c["theme"] in themes, f"Bad theme: {c['theme']} in {c['name_en']}"
```

### 2. API 모듈 import 테스트

```python
# tests/test_api_import.py
def test_gemini_api_imports():
    from api.claude_api import curate_in_english, generate_plogging_route

def test_tour_api_imports():
    from api.tour_api import get_nearby_restaurants, get_nearby_accommodations, format_place
```

### 3. 코스 스키마 필드 테스트

```python
# tests/test_schema.py
REQUIRED_KEYS = [
    "id", "name", "name_en", "start", "end", "start_en", "end_en",
    "distance_km", "difficulty", "duration_hours", "lat", "lon",
    "theme", "highlights_en", "description_en", "pet_friendly",
    "plogging_tip", "official_map_url", "kakao_map_url"
]

@pytest.mark.parametrize("courses,coords,themes", REGIONS)
def test_required_keys_present(courses, coords, themes):
    for c in courses:
        for key in REQUIRED_KEYS:
            assert key in c, f"Missing key '{key}' in {c.get('name_en', c.get('id'))}"
```

## 실행 방법

```bash
# 전체 테스트
pytest tests/ -v

# 특정 테스트
pytest tests/test_course_data.py::test_highlights_have_coords -v
```

## 금지 사항

- ❌ 코드 먼저 작성 후 테스트 붙이기
- ❌ 테스트 없이 "수동으로 확인했다"
- ❌ 테스트가 즉시 통과하는 것 (실패를 먼저 봐야 함)
- ❌ 한 테스트에 여러 동작 검증
