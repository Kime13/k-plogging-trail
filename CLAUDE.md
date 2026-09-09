# CLAUDE.md — K-Plogging Trail

@AGENTS.md

## 프로젝트 스킬

아래 스킬 파일을 반드시 읽고 해당 작업 시 지침을 따르라:

- @.agents/skills/superpowers/SKILL.md — **모든 작업 시작 전** 관련 스킬 강제 호출
- @.agents/skills/course-data-expert/SKILL.md — 코스 데이터 추가·수정 시
- @.agents/skills/streamlit-ui-expert/SKILL.md — UI 컴포넌트·스타일 작업 시

## Claude 전용 지침

- 이 프로젝트의 모든 컨텍스트는 AGENTS.md를 참조하라
- 코드 수정 시 기존 Streamlit CSS 스타일 컨벤션을 유지하라
- 커밋 메시지는 영문으로 작성하라 (예: `Fix highlight coordinates for Busan routes`)
- `api/claude_api.py` 파일명은 레거시이며 내부적으로 Gemini API를 사용한다
- 환경변수는 `.env` 파일에 저장되며 `python-dotenv`로 로드한다
