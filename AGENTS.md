# NovelAgent v0.1 — Codex Project Instructions

## Mission
Build NovelAgent, a highly autonomous long-form web-novel creation agent.

The agent must take a high-level author goal, autonomously plan and execute most work, maintain structured long-term novel memory, detect inconsistencies, and ask the author only for decisions that materially affect the book.

## Author relationship
The author is the final decision maker. Default autonomy level: 5/5.

The agent should:
- make ordinary creative and implementation decisions itself;
- proactively identify the next useful task;
- avoid unnecessary questions;
- challenge weak ideas constructively;
- preserve established canon;
- pause only for decisions with major downstream consequences.

## Decision policy
GREEN — decide autonomously:
- names, minor characters, ordinary locations;
- scene transitions;
- routine dialogue and prose;
- minor plot details;
- ordinary world-building that does not contradict canon.

YELLOW — decide and record, but keep reversible:
- moderate subplot changes;
- minor character fate changes;
- scene rearrangement;
- local pacing revisions.

RED — ask the author before committing:
- core premise changes;
- protagonist identity or fundamental goal changes;
- core world-rule changes;
- ending or central-mystery changes;
- major relationship replacement;
- broad retcons;
- major genre, audience, or tone changes.

When asking a RED decision, provide the decision, why it matters, 2–4 viable options, consequences, and concise advice.

## Long-form principles
1. Optimize for reader engagement, not empty spectacle.
2. Maintain cause and effect.
3. Every major arc should change story state.
4. Avoid padding.
5. Track unresolved promises, mysteries, conflicts, and foreshadowing.
6. Respect character knowledge boundaries.
7. Never silently contradict locked canon.
8. Prefer reversible changes until major directions are approved.
9. Update project memory after meaningful work.
10. Inspect current project state before each major phase.

## Memory
Use human-readable Markdown/JSON first. v0.1 should not require a database or vector store.

Canonical memory:
- memory/CANON.md
- memory/world/
- memory/characters/
- memory/story/
- memory/foreshadowing/
- memory/timeline/
- memory/current_state.md

Manuscript:
- manuscript/

## Agent loop
OBSERVE → RETRIEVE → IDENTIFY OBJECTIVE → PLAN → EXECUTE → SELF-CHECK → UPDATE MEMORY → CONTINUE / ASK / FINISH

## Coding principles
- Small, testable modules.
- Provider/model integration must remain replaceable.
- Human-readable file formats.
- Explicit state.
- Tests for state transitions and memory updates.
- No UI before the core workflow is testable.
- No premature infrastructure.

## v0.1 scope
Build:
- Python 3.12+;
- LangGraph;
- SQLite;
- Markdown project memory;
- provider-agnostic model interface;
- project initialization;
- state loading;
- decision classification;
- author approval pause/resume;
- memory update;
- basic tests;
- CLI entry point.

Do NOT implement React, PostgreSQL, pgvector, Redis, Celery, or multi-agent orchestration in v0.1.

## Definition of done
A developer can initialize a novel project, give a high-level goal, see the agent create project state, have it pause for a RED decision when appropriate, approve that decision, resume, and update project memory.

Implement the smallest working version; do not merely produce architecture documents.
