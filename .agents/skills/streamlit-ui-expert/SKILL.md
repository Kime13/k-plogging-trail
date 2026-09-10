---
name: streamlit-ui-expert
description: K-Plogging Trail Streamlit UI 스타일 가이드 스킬. CSS 테마 컨벤션, 컴포넌트 패턴, 커스텀 HTML 규칙을 정의한다.
---

# Streamlit UI Expert

## 트리거

- 새 Streamlit 페이지 추가
- UI 컴포넌트 수정 또는 스타일 변경
- 반응형 레이아웃 관련 작업

## 테마 컬러 시스템

`.streamlit/config.toml` 기준:

| 토큰 | 값 | 용도 |
|------|-----|------|
| `primaryColor` | `#2D6A4F` | 메인 그린, 헤더, 강조 텍스트 |
| `backgroundColor` | `#F7F3EE` | 페이지 배경 (따뜻한 베이지) |
| `secondaryBackgroundColor` | `#EDE8E0` | 사이드바, 보조 카드 배경 |
| `textColor` | `#1a1a1a` | 기본 텍스트 |

### 보조 색상 (CSS에서 사용)

| 색상 | 값 | 용도 |
|------|-----|------|
| 그린 그라데이션 | `#2D6A4F → #40916C` | 코스 헤더 배경 |
| 라이트 그린 | `#D8F3DC` | 정보 배너 |
| 보더 | `#D4C9B8` | 카드 테두리 |
| 난이도 Easy | `#2D6A4F` | 초록 |
| 난이도 Moderate | `#856404` | 갈색 |
| 난이도 Challenge | `#842029` | 빨강 |

## CSS 클래스 컨벤션

프로젝트에서 사용하는 주요 CSS 클래스:

| 클래스 | 용도 |
|--------|------|
| `.course-header` | 코스 상세 상단 배너 (그라데이션) |
| `.info-banner` | 정보 안내 (좌측 보더) |
| `.metric-card` | 통계 수치 카드 |
| `.route-box` | AI 생성 루트 표시 |
| `.tip-box` | 플로깅 팁 박스 |
| `.place-card` | 맛집/숙소 카드 |
| `.hero-card` | 랜딩 페이지 메인 카드 |

## UI 작성 규칙

1. **`unsafe_allow_html=True`** 사용 시 반드시 `st.markdown()`으로 래핑
2. **CSS는 각 페이지 상단**에 `<style>` 블록으로 배치
3. **인라인 HTML**에서는 f-string 사용, 따옴표 충돌 주의 (외부 `"""`, 내부 `'`)
4. **카드 컴포넌트** 기본 스타일:
   ```css
   background: white;
   border-radius: 12px;
   padding: 16px;
   border: 1px solid #D4C9B8;
   box-shadow: 0 2px 8px rgba(0,0,0,0.06);
   ```
5. **이모지**를 제목 앞에 사용하여 시각적 구분 (예: `### 🍽️ After Your Plogging`)

## 새 페이지 추가 시 체크리스트

1. [ ] `pages/N_이모지_PageName.py` 형식으로 파일 생성
2. [ ] 페이지 상단에 `.stApp` 배경색 CSS 추가
3. [ ] `st.set_page_config()` 설정 (주의: Streamlit 경고 가능)
4. [ ] 사이드바 사용 시 `#EDE8E0` 배경색 지정
