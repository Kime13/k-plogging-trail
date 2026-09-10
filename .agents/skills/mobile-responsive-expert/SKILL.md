---
name: mobile-responsive-expert
description: 외국인 관광객의 모바일 사용 비중이 높으므로, Streamlit 앱의 모바일 반응형 CSS와 터치 친화적 UI를 최적화한다.
---

# Mobile Responsive Expert — Streamlit 모바일 최적화

## 왜 중요한가

K-Plogging Trail의 주 사용자는 **한국을 여행 중인 외국인 관광객**이다.
여행 중에는 대부분 **모바일로 접속**하므로 모바일 최적화는 핵심이다.

## Streamlit 모바일 제약

Streamlit은 Tailwind/CSS 프레임워크 없이 `unsafe_allow_html=True`로 커스텀 CSS를 주입한다.
따라서 반응형은 **미디어 쿼리를 직접 작성**해야 한다.

## 반응형 브레이크포인트

| 기기 | 너비 | 적용 |
|------|------|------|
| 모바일 | < 640px | 단일 컬럼, 카드 풀 와이드 |
| 태블릿 | 640-1024px | 2컬럼까지 |
| 데스크톱 | > 1024px | 현재 레이아웃 유지 |

## CSS 패턴

### 1. 랜딩 페이지 `.hero-card` 반응형

```css
/* app.py 랜딩 페이지 */
@media (max-width: 640px) {
    .hero-card {
        width: 90vw !important;
        height: auto !important;
        min-height: 360px;
        border-radius: 24px !important;
        padding: 24px 16px !important;
    }
    .hero-title { font-size: 1.5rem !important; }
    .hero-subtitle { font-size: 0.85rem !important; }
    .hero-badge { font-size: 0.75rem !important; padding: 8px 14px !important; }
}
```

### 2. Course Finder 카드 반응형

```css
/* Course Finder 코스 카드 */
@media (max-width: 640px) {
    .course-header h2 { font-size: 1.2rem !important; }
    .metric-card { padding: 10px !important; }
    .metric-card .value { font-size: 1.3rem !important; }
    .place-card { padding: 10px !important; }
}
```

### 3. 지도 높이 조정

```css
@media (max-width: 640px) {
    /* Folium 지도 iframe */
    iframe { height: 300px !important; }
}
```

### 4. 터치 영역 보장

```css
/* 모든 버튼·링크 최소 터치 영역 */
@media (max-width: 640px) {
    .stButton > button {
        min-height: 48px !important;
        font-size: 1rem !important;
    }
    a { padding: 12px 0 !important; }
}
```

## 체크리스트

모바일 관련 작업 시:

1. [ ] 640px 이하에서 가로 스크롤이 발생하지 않는가?
2. [ ] 카드·버튼이 화면 너비를 초과하지 않는가?
3. [ ] 터치 가능한 요소가 최소 48x48px인가?
4. [ ] 지도가 화면 내에 적절히 표시되는가?
5. [ ] 텍스트가 잘리지 않고 읽을 수 있는 크기인가?
6. [ ] `st.columns(4)` 등 다단 레이아웃이 모바일에서 깨지지 않는가?

## Streamlit 모바일 팁

- `st.columns(N)` — 모바일에서 Streamlit이 자동으로 세로 배치하지만, 커스텀 HTML은 직접 처리 필요
- `layout="wide"` — 모바일에서 여백이 너무 좁아질 수 있음
- 공식 지도 버튼 — 모바일에서 버튼 2개 가로 배치 시 겹침 주의

## 검증 방법

```
Chrome DevTools → 모바일 에뮬레이터
→ iPhone SE (375px), iPhone 12 (390px), Galaxy S21 (360px)
→ 랜딩 → Course Finder → 코스 선택 → 지도 → Impact Dashboard
```
