# NovelAgent v0.1

A highly autonomous long-form novel creation agent designed to run as a Codex project.

## Goal
Give the agent a high-level objective such as:

> 我要写一本东方诡异修仙长篇小说。

The agent should take responsibility for planning and progressing the project, while asking the author only for major decisions.

## Stack
- Python 3.12+
- LangGraph
- SQLite
- Markdown / JSON project memory
- Provider-agnostic LLM adapter

## v0.1 intentionally excludes
- React UI
- PostgreSQL
- pgvector
- Redis
- Celery
- multi-agent orchestration

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## First run

```bash
novel-agent init ./my-novel
novel-agent run ./my-novel "我要写一本东方诡异修仙长篇小说"
```

The exact CLI may evolve during implementation; `AGENTS.md` is the authoritative development instruction.

## Development rule
The first milestone is a working stateful loop, not a polished interface.
