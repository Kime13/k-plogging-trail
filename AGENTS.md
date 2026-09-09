# AGENTS.md — K-Plogging Trail

> AI 에이전트가 이 프로젝트를 이해하고 작업하기 위한 핵심 컨텍스트 문서

## 프로젝트 개요

외국인 관광객 대상 한국 플로깅(Plogging = Jogging + Picking up trash) 코스 안내 웹 애플리케이션.
제주 올레길, 서울 둘레길, 부산 갈맷길 14개 코스를 Gemini AI 큐레이션과 함께 제공한다.

## 기술 스택

- **프레임워크**: Streamlit (멀티페이지 앱)
- **지도**: Folium + streamlit-folium
- **차트**: Plotly Express
- **AI**: Google Gemini (`google-genai` SDK)
- **DB**: Supabase (PostgreSQL)
- **외부 API**: 한국관광공사 TourAPI, Kakao Maps, OSRM
- **언어**: Python 3.10+

## 디렉터리 구조

```
k-plogging-trail/
├── app.py                      # 랜딩 페이지 + 메인 허브
├── requirements.txt            # 의존성
├── .streamlit/config.toml      # Streamlit 테마
├── api/
│   ├── claude_api.py           # Gemini AI 큐레이션 (파일명 레거시)
│   └── tour_api.py             # 한국관광공사 OpenAPI
├── pages/
│   ├── 1_🗺️_Course_Finder.py  # 코스 탐색·지도·AI 루트
│   └── 2_♻️_Impact_Dashboard.py # 플로깅 기록·통계
└── utils/
    ├── busan_courses.py        # 부산 갈맷길 코스 데이터
    ├── helpers.py              # OSRM 도보 경로
    ├── jeju_olle.py            # 제주 올레 코스 데이터
    ├── kakao_coords.py         # 카카오 좌표 조회 (개발 스크립트)
    └── seoul_courses.py        # 서울 둘레길 코스 데이터
```

## 핵심 데이터 구조

### 코스 데이터 스키마

모든 코스 데이터(`utils/*_courses.py`)는 아래 구조를 따른다:

```python
{
    "id": str | int,            # 고유 식별자
    "name": str,                # 한글 코스명
    "name_en": str,             # 영문 코스명
    "start": str,               # 한글 시작점
    "end": str,                 # 한글 종점
    "start_en": str,            # 영문 시작점
    "end_en": str,              # 영문 종점
    "distance_km": float,       # 거리 (km)
    "difficulty": str,          # "Easy" | "Moderate" | "Challenge"
    "duration_hours": float,    # 소요 시간
    "lat": float,               # 시작점 위도
    "lon": float,               # 시작점 경도
    "theme": str,               # 테마 키 (coastal, mountain, park 등)
    "highlights_en": list[str], # 주요 명소 (영문) — 최대 3개
    "description_en": str,      # 영문 설명 (2-3문장)
    "pet_friendly": bool,       # 반려동물 동반 가능 여부
    "plogging_tip": str,        # 플로깅 팁
    "official_map_url": str,    # 공식 지도 URL
    "kakao_map_url": str,       # 카카오맵 URL
}
```

### 지역 추가 방법

1. `utils/` 아래에 `{region}_courses.py` 생성
2. `COURSES`, `HIGHLIGHT_COORDS`, `THEMES` 3개 변수 export
3. `pages/1_🗺️_Course_Finder.py`의 `REGION_DATA`에 추가

## 환경변수

| 변수 | 용도 | 필수 |
|------|------|------|
| `GEMINI_API_KEY` | Gemini AI | ✅ |
| `TOUR_API_KEY` | 한국관광공사 TourAPI | ✅ |
| `SUPABASE_URL` | Supabase URL | ✅ |
| `SUPABASE_KEY` | Supabase anon key | ✅ |
| `KAKAO_API_KEY` | 카카오 좌표 (개발용) | 선택 |

## 코딩 규칙

- UI 텍스트는 **영문 우선** (외국인 대상 서비스)
- 주석·docstring은 한글 허용
- Streamlit `unsafe_allow_html=True`로 커스텀 CSS/HTML 사용
- 코스 데이터의 `highlights_en` 키는 `HIGHLIGHT_COORDS` 딕셔너리의 키와 **정확히 일치**해야 함
- 난이도는 반드시 `"Easy"`, `"Moderate"`, `"Challenge"` 중 하나

## 주의 사항

- `api/claude_api.py`는 이름과 달리 **Gemini API**를 사용함 (레거시 네이밍)
- `utils/helpers.py`, `utils/kakao_coords.py`는 현재 앱에서 import되지 않음 (개발 유틸)
- `pages/` 파일에 `set_page_config()`가 있으면 Streamlit 경고 발생 가능
- Supabase 테이블명: `plogging_logs`

## 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# 환경변수 설정
cp .env.example .env  # 환경변수 편집

# 실행
streamlit run app.py
```
