---
name: provide-test-for-human
description: 기능 완성 후 사용자가 직접 검증할 수 있도록 클릭 가능한 URL, 테스트 시나리오, 입력 데이터를 표 형식으로 제공한다.
---

# Provide Test for Human — 사용자 수동 검증 가이드

## 적용 시점

- "테스트 해볼 방법?", "어떻게 확인해?"
- 코스 추가 후 검증 필요
- UI 변경 후 육안 확인 필요
- API 연동 변경 후 동작 확인 필요

## 핵심 규칙

### 1. 클릭 가능한 링크 제공

```markdown
# ✅ 올바른 방식
[K-Plogging Trail 메인](http://localhost:8501)
[Course Finder](http://localhost:8501/Course_Finder)
[Impact Dashboard](http://localhost:8501/Impact_Dashboard)

# ❌ 잘못된 방식
http://localhost:8501 에 접속하세요
```

### 2. Streamlit URL 구조

| 페이지 | URL |
|--------|-----|
| 랜딩 | `http://localhost:8501` |
| Course Finder | `http://localhost:8501/Course_Finder` |
| Impact Dashboard | `http://localhost:8501/Impact_Dashboard` |

### 3. 테스트 시나리오 표

기능 변경 후 반드시 아래 형식으로 테스트 가이드를 제공한다:

| # | 시나리오 | 조작 | 기대 결과 |
|---|---------|------|-----------|
| 1 | 제주 코스 필터 | 🗺️ Jeju → 💪 Easy | Easy 코스만 표시 |
| 2 | 서울 코스 지도 | Route 4 → 🏃 Start | 지도에 마커 3개 표시 |
| 3 | 반려동물 필터 | 🐾 체크 | Pet-friendly 코스만 |
| 4 | AI 루트 생성 | 아무 코스 → Start | 루트 박스에 텍스트 표시 |
| 5 | 플로깅 기록 | ➕ Log → 0.5kg | "✅ Logged!" 메시지 |

### 4. 코스 데이터 변경 시 추가 검증

| 대상 | 검증 방법 | 기대 결과 |
|------|-----------|-----------|
| 새 코스 | 해당 지역 선택 → 코스 목록 확인 | 새 코스가 목록에 표시 |
| 좌표 변경 | 코스 선택 → 지도 확인 | 마커가 올바른 위치에 표시 |
| 하이라이트 | 코스 선택 → ⭐ Highlights 확인 | 3개 하이라이트 모두 표시 |
| 테마 필터 | 🎨 Theme 필터 선택 | 해당 테마 코스만 필터링 |

### 5. 환경 준비 안내

```bash
# 앱 실행
streamlit run app.py

# 환경변수 확인 (API 테스트 시)
echo "GEMINI_API_KEY: ${GEMINI_API_KEY:+SET}"
echo "TOUR_API_KEY: ${TOUR_API_KEY:+SET}"
echo "SUPABASE_URL: ${SUPABASE_URL:+SET}"
```

## 출력 형식 예시

```markdown
## 🧪 수동 테스트 가이드

**앱 실행:** `streamlit run app.py` → [http://localhost:8501](http://localhost:8501)

| # | 시나리오 | 조작 | 기대 결과 |
|---|---------|------|-----------|
| 1 | [구체적 시나리오] | [구체적 조작] | [구체적 결과] |

**주의:** [특이사항이 있으면 명시]
```
