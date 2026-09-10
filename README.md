# 🌿 K-Plogging Trail

> **Run. Pick. Make Korea Cleaner.**
>
> 외국인 관광객을 위한 한국 플로깅(Plogging) 코스 안내 웹 애플리케이션

## ✨ Features

- 🗺️ **Course Finder** — 제주·서울·부산 14개 플로깅 코스를 난이도·테마·반려동물 동반 여부로 필터링
- 🤖 **AI Curation** — Gemini AI가 각 명소를 외국인 관점에서 영문 큐레이션
- 🏃 **Route Generator** — 난이도별 플로깅 루트 자동 생성 (Stop-by-stop 가이드)
- 🗺️ **Interactive Map** — Folium 지도 + 주변 맛집·숙소 표시 (한국관광공사 OpenAPI)
- ♻️ **Impact Dashboard** — 플로깅 기록 저장 + 누적 환경 임팩트 시각화
- 🔗 **Official Maps** — 공식 지도 + 카카오맵 바로가기 링크

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit · Folium · Plotly |
| AI | Google Gemini (google-genai) |
| Database | Supabase (PostgreSQL) |
| APIs | 한국관광공사 TourAPI · Kakao Maps · OSRM |

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 저장소 클론
git clone https://github.com/Kime13/k-plogging-trail.git
cd k-plogging-trail

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### Environment Variables

`.env.example`을 복사한 뒤, 실제 API 키를 입력하세요:

```bash
cp .env.example .env
```

`.env` 파일을 열어 `your_..._here` 부분을 실제 키로 교체합니다:

```env
GEMINI_API_KEY=your_gemini_api_key_here
TOUR_API_KEY=your_tour_api_key_here
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your_supabase_anon_key_here
# KAKAO_API_KEY=your_kakao_api_key_here  # 선택 (개발용)
```

| 변수 | 필수 | 발급처 | 용도 |
|------|:---:|--------|------|
| `GEMINI_API_KEY` | ✅ | [Google AI Studio](https://aistudio.google.com/apikey) | AI 코스 설명 + 루트 생성 |
| `TOUR_API_KEY` | ✅ | [공공데이터포털](https://www.data.go.kr/) | 주변 관광지 추천 |
| `SUPABASE_URL` | ✅ | [Supabase](https://supabase.com/) → Settings → API | 플로깅 기록 저장 |
| `SUPABASE_KEY` | ✅ | [Supabase](https://supabase.com/) → Settings → API | 플로깅 기록 저장 |
| `KAKAO_API_KEY` | 선택 | [Kakao Developers](https://developers.kakao.com/) | 좌표 조회 (개발용) |

### Run

```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501` 로 접속하세요.

## 📂 Project Structure

```
k-plogging-trail/
├── app.py                      # 랜딩 페이지 + 메인 허브
├── requirements.txt            # 의존성
├── .streamlit/config.toml      # Streamlit 테마
├── api/
│   ├── claude_api.py           # Gemini AI 큐레이션
│   └── tour_api.py             # 한국관광공사 OpenAPI
├── pages/
│   ├── 1_🗺️_Course_Finder.py  # 코스 탐색·지도·AI 루트
│   └── 2_♻️_Impact_Dashboard.py # 기록·통계 대시보드
└── utils/
    ├── busan_courses.py        # 부산 갈맷길 데이터
    ├── helpers.py              # OSRM 도보 경로
    ├── jeju_olle.py            # 제주 올레 데이터
    ├── kakao_coords.py         # 카카오 좌표 조회
    └── seoul_courses.py        # 서울 둘레길 데이터
```

## 🗺️ Supported Courses

### 🌿 Jeju Olle (6 courses)

Route 1, 1-1 (Udo), 6, 10, 14, 21

### 🏙️ Seoul Dulegil (4 courses)

Route 4, 5, 15, 19

### 🌊 Busan Galmaetgil (4 courses)

Route 1-1, 3-2, 4-1, 8-2

## 🤝 Credits

- **한국관광공사** — TourAPI 데이터
- **제주올레** — 올레길 코스 정보
- **서울시** — 서울둘레길 코스 정보
- **부산시** — 갈맷길 코스 정보
- **Google Gemini** — AI 큐레이션
- **WanderRabbit 🐰** — 기획 및 개발

## 📄 License

This project is for educational purposes.
