# Reflexion System

> **Status: Under Active Development** — This project is not yet production-ready. Core architecture is scaffolded; implementation is in progress.

An LLM-powered autonomous coding agent that uses **reflexion** — a self-reflective feedback loop — to iteratively plan, write, execute, evaluate, and improve code until a task is solved or a retry limit is reached.

Inspired by the [Reflexion paper](https://arxiv.org/abs/2303.11366) (Shinn et al., 2023), the system treats failures as learning signals rather than terminal states, feeding execution errors and evaluator feedback back into the loop to produce progressively better solutions.

## How It Works

```
Task → Planner → Coder → Executor → Evaluator
                                        │
                              ┌─────────┤
                              │ Pass    │ Fail
                              ▼         ▼
                           Done     Reflector
                                        │
                                        ▼
                                 Retry (Coder)
```

1. **Planner** — Interprets the raw task and produces a step-by-step plan.
2. **Coder** — Generates Python code from the plan (or a revised plan after reflection).
3. **Executor** — Runs the generated code in a sandboxed environment and captures output/errors.
4. **Evaluator** — Judges whether the output satisfies the original task.
5. **Reflector** — On failure, analyzes what went wrong and produces a new strategy for the next attempt.
6. **Control Loop** — Orchestrates the above agents, manages immutable state transitions, and enforces the retry limit.

The loop continues until the evaluator marks the task as **passed** or the maximum retry count (`MAX_RETRIES`) is reached.

## Project Structure

```
Reflexion System/
├── main.py                  # Entry point
├── config.py                # Centralized configuration
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not committed)
├── app/
│   ├── __init__.py
│   ├── control_loop.py      # Core loop + immutable ReflexionState
│   ├── planner.py           # Task interpretation & planning agent
│   ├── coder.py             # Code generation agent
│   ├── executor_tool.py     # Sandboxed code execution
│   ├── evaluator.py         # Output evaluation agent
│   ├── reflector.py         # Failure analysis & strategy revision agent
│   ├── state.py             # Shared state definitions
│   └── prompts/
│       ├── planner_prompt.txt
│       ├── coder_prompt.txt
│       ├── evaluator_prompt.txt
│       └── reflector_prompt.txt
└── tests/
    └── test_tasks.py        # Task-level integration tests
```

## Setup

### Prerequisites

- Python 3.10+
- An API key for your chosen LLM provider (OpenAI or Google)

### Installation

```bash
# Clone the repository
git clone https://github.com/GitTanish/Reflexion-System.git
cd Reflexion-System

# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` or populate `.env` with your values:

```env
# LLM API Keys
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=AIza...

# Model Configuration
MODEL_NAME=gpt-4
TEMPERATURE=0.2
MAX_TOKENS=4096

# Execution
MAX_RETRIES=3
```

## Current Progress

| Component | Status |
|---|---|
| File structure & scaffolding | Done |
| `ReflexionState` (immutable dataclass) | Done |
| Control loop skeleton | Done |
| Planner agent | Not started |
| Coder agent | Not started |
| Executor (sandboxed runner) | Not started |
| Evaluator agent | Skeleton / Mocked |
| Reflector agent | Not started |
| Prompt templates | Not started |
| Config / env loading | Not started |
| Entry point (`main.py`) | Not started |
| Tests | Not started |

## Key Design Decisions

- **Immutable state** — `ReflexionState` is a frozen dataclass. Every iteration produces a new state via `dataclasses.replace()`, making the execution history fully traceable and side-effect-free.
- **Prompt-driven agents** — Each agent (planner, coder, evaluator, reflector) is backed by a dedicated prompt template, keeping LLM instructions separated from code logic.
- **Configurable retry budget** — The maximum number of reflexion iterations is controlled by `MAX_RETRIES`, preventing infinite loops and runaway API costs.

## License

TBD
