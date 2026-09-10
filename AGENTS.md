# AGENTS.md — K-Plogging Trail (SSOT)

> **이 파일이 프로젝트의 Single Source of Truth (SSOT)이다.**
> 모든 AI 에이전트(Claude Code, Antigravity, Gemini 등)는 이 문서를 기준으로 동작한다.
> 플랫폼별 설정 파일(CLAUDE.md, .gemini/ 등)은 이 문서를 참조하는 얇은 래퍼일 뿐이다.

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
├── AGENTS.md                   # ★ SSOT — AI 에이전트 공유 컨텍스트
├── CLAUDE.md                   # Claude Code 래퍼 (→ AGENTS.md 참조)
├── README.md                   # 프로젝트 소개 문서
├── app.py                      # 랜딩 페이지 + 메인 허브
├── requirements.txt            # 의존성
├── .streamlit/config.toml      # Streamlit 테마
├── .agents/skills/             # AI 에이전트 스킬 (12개)
│   ├── superpowers/            # 메타: 스킬 강제 호출
│   ├── brainstorming/          # 프로세스: 기능 구조화
│   ├── systematic-debugging/   # 프로세스: 근본 원인 추적
│   ├── writing-plans/          # 프로세스: 구현 계획
│   ├── explain-before-act/     # 프로세스: 작업 전 설명
│   ├── course-data-expert/     # 구현: 코스 데이터 스키마
│   ├── streamlit-ui-expert/    # 구현: UI 스타일 가이드
│   ├── mobile-responsive-expert/ # 구현: 모바일 반응형
│   ├── verification-before-completion/ # 품질: 완료 검증
│   ├── ralph-loop/             # 품질: 끝까지 해결
│   ├── test-driven-development/ # 품질: TDD
│   └── provide-test-for-human/ # 품질: 수동 검증 가이드
├── api/
│   ├── gemini_api.py           # Gemini AI 큐레이션
│   └── tour_api.py             # 한국관광공사 OpenAPI
├── pages/
│   ├── 1_🗺️_Course_Finder.py  # 코스 탐색·지도·AI 루트 (오케스트레이터)
│   └── 2_♻️_Impact_Dashboard.py # 플로깅 기록·통계
└── utils/
    ├── busan_courses.py        # 부산 갈맷길 코스 데이터
    ├── helpers.py              # OSRM 도보 경로 (미사용)
    ├── jeju_olle.py            # 제주 올레 코스 데이터
    ├── kakao_coords.py         # 카카오 좌표 조회 (미사용, 개발 스크립트)
    ├── map_builder.py          # Folium 지도 생성·마커 추가
    ├── seoul_courses.py        # 서울 둘레길 코스 데이터
    └── ui_components.py        # Course Finder UI 컴포넌트 (CSS·카드·명소)
```

## 스킬 체계

12개 스킬이 `.agents/skills/`에 있으며, 아래 순서로 호출한다:

```
메타        superpowers ─── 모든 작업 전 스킬 강제 호출
             ↓
프로세스    brainstorming → writing-plans (기능 추가)
            systematic-debugging (버그 수정)
            explain-before-act (모든 작업)
             ↓
구현        course-data-expert (코스 데이터)
            streamlit-ui-expert (UI)
            mobile-responsive-expert (모바일)
             ↓
품질        test-driven-development (TDD)
            verification-before-completion (완료 검증)
            ralph-loop (끝까지 해결)
            provide-test-for-human (수동 검증)
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
2. `{REGION}_COURSES`, `{REGION}_HIGHLIGHT_COORDS`, `{REGION}_THEMES` 3개 변수 export
3. `pages/1_🗺️_Course_Finder.py`의 `REGION_DATA`에 추가
4. `pages/2_♻️_Impact_Dashboard.py`의 `all_courses` 리스트에 import 추가

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

## 커뮤니케이션 규칙

- 프로젝트 오너는 비개발자이므로, **모든 설명은 비개발자가 이해할 수 있도록 쉽게 풀어서 작성**한다
- 기술 용어를 사용할 때는 반드시 일상 비유나 한 줄 설명을 함께 달아야 한다
- 이슈, 커밋 본문, 리뷰 코멘트 모두 이 원칙을 따른다

## 주의 사항

- `utils/helpers.py`, `utils/kakao_coords.py`는 현재 앱에서 import되지 않음 (개발 유틸)
- `utils/ui_components.py`, `utils/map_builder.py`는 `pages/1_Course_Finder.py`에서 import하는 UI/지도 모듈
- `pages/` 파일에 `set_page_config()`가 있으면 Streamlit 경고 발생 가능
- Supabase 테이블명: `plogging_logs`

## 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# 환경변수 설정 (.env 파일 생성)
cat > .env << 'EOF'
GEMINI_API_KEY=your_key_here
TOUR_API_KEY=your_key_here
SUPABASE_URL=your_url_here
SUPABASE_KEY=your_key_here
EOF

# 실행
streamlit run app.py
```
