---
name: writing-plans
description: brainstorming에서 확정된 설계를 구현 계획으로 변환한다. 다단계 작업 전 반드시 사용.
---

# Writing Plans — 구현 계획 작성

brainstorming에서 승인된 설계를 엔지니어가 바로 실행할 수 있는 단계별 계획으로 변환한다.

**저장 경로:** `docs/plans/YYYY-MM-DD-<기능명>.md`

## 계획 문서 헤더

```markdown
# [기능명] 구현 계획

**목표:** [한 줄]
**기술:** Streamlit · Folium · Gemini · Supabase (해당하는 것만)

## 전역 제약

- UI 텍스트는 영문 우선
- 코스 데이터는 AGENTS.md 스키마 준수
- highlights_en ↔ HIGHLIGHT_COORDS 정합성 필수
- difficulty: "Easy" | "Moderate" | "Challenge"
---
```

## 태스크 구조

```markdown
### Task N: [컴포넌트명]

**파일:**
- 생성: `정확한/경로/파일.py`
- 수정: `정확한/경로/기존파일.py`

**단계:**
- [ ] Step 1: [구체적 작업 — 코드 포함]
- [ ] Step 2: [검증 방법]
- [ ] Step 3: 커밋
```

## K-Plogging Trail 태스크 패턴

### 새 코스 지역 추가

```
Task 1: 코스 데이터 파일 생성
  - 생성: utils/{region}_courses.py
  - COURSES, HIGHLIGHT_COORDS, THEMES 3개 변수

Task 2: Course Finder 연동
  - 수정: pages/1_🗺️_Course_Finder.py
  - REGION_DATA 딕셔너리에 추가
  - import 추가

Task 3: Impact Dashboard 연동
  - 수정: pages/2_♻️_Impact_Dashboard.py
  - all_courses 리스트에 import 추가

Task 4: 검증
  - streamlit run app.py
  - 새 지역 선택 → 코스 목록 → 지도 마커 → AI 루트
```

### 새 페이지 추가

```
Task 1: 페이지 파일 생성
  - 생성: pages/N_이모지_Name.py
  - CSS 테마 (.stApp 배경, 사이드바 배경)

Task 2: 메인 허브 연결
  - 수정: app.py
  - st.page_link() 추가

Task 3: 검증
  - 랜딩 → 허브 → 새 페이지 이동 확인
```

## 규칙

- **플레이스홀더 금지** — "TBD", "나중에 구현" 없이 실제 코드 포함
- **한 태스크 = 하나의 독립적 변경** — 단독으로 테스트 가능
- **DRY · YAGNI** — 중복 제거, 불필요 기능 추가 금지
- **각 태스크 끝에 커밋** — 작은 단위로 히스토리 보존
