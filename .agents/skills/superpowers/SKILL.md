---
name: superpowers
description: 모든 작업 시작 전 관련 스킬을 반드시 찾아 호출하도록 강제하는 메타 스킬. 1%라도 관련 가능성이 있으면 스킬을 호출해야 한다.
---

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## The Rule

**Invoke relevant skills BEFORE any response or action** — including clarifying questions, exploring the codebase, or checking files.

Then announce "Using [skill] to [purpose]" and follow the skill exactly.

## Skill Priority

Process skills come first, then implementation skills:

- "새 코스 추가해줘" → `brainstorming` first, then `course-data-expert`
- "지도 마커가 안 보여" → `systematic-debugging` first, then domain skills
- "UI 스타일 바꿔줘" → `brainstorming` first, then `streamlit-ui-expert`

## K-Plogging Trail 스킬 맵

### 프로세스 스킬 (Process — 먼저 호출)

| 스킬 | 트리거 |
|------|--------|
| `brainstorming` | 기능 추가, 새 페이지, 새 코스 지역 |
| `systematic-debugging` | 버그, API 실패, 지도 오류 |
| `explain-before-act` | 모든 작업 시작 전 |
| `writing-plans` | 다단계 작업 계획 수립 |

### 구현 스킬 (Implementation — 프로세스 후 호출)

| 스킬 | 트리거 |
|------|--------|
| `course-data-expert` | 코스·좌표·하이라이트 데이터 작업 |
| `streamlit-ui-expert` | CSS, 컴포넌트, 레이아웃 작업 |

### 품질 스킬 (Quality — 완료 전 호출)

| 스킬 | 트리거 |
|------|--------|
| `verification-before-completion` | 작업 완료 선언 전 |
| `ralph-loop` | 테스트/빌드 실패 시 끝까지 해결 |

## Red Flags

이런 생각이 들면 STOP — 합리화하고 있는 것이다:

| 생각 | 현실 |
|------|------|
| "이건 그냥 간단한 질문" | 질문도 작업. 스킬 체크. |
| "먼저 파일을 좀 봐야…" | 스킬이 HOW를 알려준다. 스킬 먼저. |
| "이건 스킬까지 필요 없어" | 스킬이 존재하면 사용해야 한다. |
| "이전에 읽었으니 기억나" | 스킬은 진화한다. 현재 버전을 읽어라. |
| "좌표 하나만 바꾸면 되잖아" | 단순한 것이 복잡해진다. 스킬 사용. |

## User Instructions

CLAUDE.md, AGENTS.md 등 사용자 지침은 스킬보다 우선한다.
스킬은 기본 동작보다 우선한다.
