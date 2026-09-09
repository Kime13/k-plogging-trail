# CLAUDE.md — K-Plogging Trail

> 이 파일은 Claude Code 전용 래퍼이다.
> **프로젝트의 SSOT(Single Source of Truth)는 AGENTS.md**이며, 이 파일은 AGENTS.md를 참조하고
> Claude Code 고유 기능(`@` 참조)으로 스킬을 연결하는 역할만 한다.

@AGENTS.md

## 스킬 참조

### 메타

- @.agents/skills/superpowers/SKILL.md — **모든 작업 시작 전** 관련 스킬 강제 호출

### 프로세스 (먼저 호출)

- @.agents/skills/brainstorming/SKILL.md — 기능 추가, 새 페이지, 새 지역 추가 전
- @.agents/skills/systematic-debugging/SKILL.md — 버그, API 실패, 지도 오류 시
- @.agents/skills/writing-plans/SKILL.md — 다단계 구현 계획 수립 시
- @.agents/skills/explain-before-act/SKILL.md — 모든 작업 시작 전 상황 설명

### 구현 (프로세스 후 호출)

- @.agents/skills/course-data-expert/SKILL.md — 코스 데이터 추가·수정 시
- @.agents/skills/streamlit-ui-expert/SKILL.md — UI 컴포넌트·스타일 작업 시
- @.agents/skills/mobile-responsive-expert/SKILL.md — 모바일 반응형 CSS 작업 시

### 품질 (완료 전 호출)

- @.agents/skills/verification-before-completion/SKILL.md — 작업 완료 선언 전 검증
- @.agents/skills/ralph-loop/SKILL.md — 실패 시 끝까지 해결
- @.agents/skills/test-driven-development/SKILL.md — 기능/버그 수정 전 테스트 먼저
- @.agents/skills/provide-test-for-human/SKILL.md — 사용자 수동 검증 가이드
