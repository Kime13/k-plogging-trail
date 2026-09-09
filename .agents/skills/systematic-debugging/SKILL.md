---
name: systematic-debugging
description: 버그, API 실패, 지도 마커 오류 등 모든 기술적 문제 발생 시 근본 원인을 먼저 추적한다. 추측 수정 금지.
---

# Systematic Debugging — 근본 원인 먼저

**핵심 원칙:** 근본 원인을 찾기 전에 수정하지 않는다. 증상 수정은 실패다.

## Phase 1: 근본 원인 조사

**수정 시도 전에 반드시 완료:**

1. **에러 메시지 정독** — 스택 트레이스, 라인 번호, 에러 코드
2. **재현** — 동일 조건에서 반복 발생하는가?
3. **최근 변경 확인** — `git diff`, 최근 커밋, 환경변수 변경
4. **데이터 흐름 추적** — 잘못된 값이 어디서 시작되는가?

### K-Plogging Trail 진단 순서

```
[1] 환경변수 확인
    └─ .env 파일 존재? GEMINI_API_KEY, TOUR_API_KEY, SUPABASE_URL/KEY 값 있는가?

[2] API 연결 확인
    ├─ Gemini: google-genai 클라이언트 초기화 성공?
    ├─ TourAPI: https://apis.data.go.kr 응답 200?
    └─ Supabase: create_client() 성공? plogging_logs 테이블 존재?

[3] 데이터 정합성 확인
    ├─ highlights_en 의 각 항목이 HIGHLIGHT_COORDS 키에 존재?
    ├─ theme 값이 THEMES 딕셔너리 키에 존재?
    └─ difficulty 값이 "Easy" | "Moderate" | "Challenge" 중 하나?

[4] Streamlit 렌더링 확인
    ├─ set_page_config 중복 호출?
    ├─ session_state 키 충돌?
    └─ unsafe_allow_html CSS 문법 오류?
```

## Phase 2: 패턴 분석

1. **동작하는 유사 코드 찾기** — 같은 코드베이스 내
2. **차이점 식별** — 동작하는 것과 깨진 것의 차이 나열
3. **의존성 확인** — 환경, 설정, 외부 API 상태

## Phase 3: 가설 검증

1. **가설 1개 수립** — "X가 원인이다, 왜냐하면 Y"
2. **최소 변경으로 검증** — 한 번에 하나만
3. **결과 확인** — 성공 → Phase 4, 실패 → 새 가설
4. **3회 실패 시** — 아키텍처 문제 의심, 사용자에게 보고

## Phase 4: 수정

1. **근본 원인 수정** — 증상이 아닌 원인
2. **동일 명령으로 재검증** — 실패했던 바로 그 조작 반복
3. **다른 코스/지역에서도 확인** — 제주만 고쳐놓고 서울이 깨지지 않았는지

## Red Flags — 즉시 멈추고 Phase 1로

- "일단 이거 바꿔보자" → 추측 수정 금지
- "아마 이게 원인일 거야" → 증거 없으면 가설에 불과
- "빨리 고쳐야 하니까" → 체계적 디버깅이 더 빠르다
- "3번째 수정인데…" → 아키텍처 문제. 사용자와 논의.
