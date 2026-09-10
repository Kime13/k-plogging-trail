---
name: verification-before-completion
description: 작업 완료를 선언하기 전에 반드시 실행 검증 증거를 확보한다. 증거 없는 완료 선언 금지.
---

# Verification Before Completion — 증거 먼저, 선언은 나중

**핵심 원칙:** 증거 없이 완료를 주장하지 않는다.

## The Iron Law

```
검증 명령을 실행하지 않았으면 "완료"라고 말할 수 없다.
```

## 검증 게이트

```
완료를 선언하기 전에:

1. IDENTIFY — 이 주장을 증명할 명령은?
2. RUN — 해당 명령 실행 (이전 실행이 아닌 지금)
3. READ — 출력 전체 확인, 종료 코드 확인
4. VERIFY — 출력이 주장을 뒷받침하는가?
   - NO → 실제 상태를 증거와 함께 보고
   - YES → 증거와 함께 완료 선언
```

## K-Plogging Trail 검증 체크리스트

### 코스 데이터 변경 시

```bash
# 1. 데이터 정합성 — Python으로 직접 검증
python -c "
from utils.{region}_courses import *
for c in COURSES:
    for h in c['highlights_en']:
        assert h in HIGHLIGHT_COORDS, f'Missing: {h}'
    assert c['difficulty'] in ('Easy','Moderate','Challenge'), f'Bad difficulty: {c[\"difficulty\"]}'
    assert c['theme'] in THEMES, f'Bad theme: {c[\"theme\"]}'
print('✅ All courses valid')
"

# 2. Streamlit 실행 확인
streamlit run app.py  # 에러 없이 로드되는지
```

### UI 변경 시

```bash
# Streamlit 실행 후 브라우저에서 확인
streamlit run app.py
# → 해당 페이지 이동
# → 변경된 컴포넌트 육안 확인
```

### API 코드 변경 시

```bash
# Python import 확인
python -c "from api.claude_api import curate_in_english, generate_plogging_route; print('✅ Import OK')"
python -c "from api.tour_api import get_nearby_restaurants, get_nearby_accommodations; print('✅ Import OK')"
```

## Red Flags — 즉시 멈춤

| 생각 | 현실 |
|------|------|
| "아마 될 거야" | 검증을 실행하라 |
| "자신 있다" | 자신감 ≠ 증거 |
| "이번만…" | 예외 없음 |
| "코드 보니까 맞다" | 코드 리뷰 ≠ 실행 검증 |
| "좌표 하나 바꿨을 뿐" | 하나가 전체를 깨뜨릴 수 있다 |

## 완료 선언 형식

```
## ✅ 검증 완료

**실행 명령:** [실행한 명령]
**결과:** PASS — [증거 요약]
**변경 파일:** [목록]
```
