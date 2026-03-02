# 🧠 Reflexion System: The Autonomous Coding Agent That *Learns* From Its Mistakes

> **🚀 Status: Under Active Development** 
> We're currently scaffolding the core architecture and bringing this beast to life. It's not production-ready yet, but the foundation is rock solid!

Ever wish your code could write itself, test itself, and—when it inevitably breaks—*fix* itself? Welcome to the **Reflexion System**.

Inspired by the groundbreaking [Reflexion paper](https://arxiv.org/abs/2303.11366) (Shinn et al., 2023), this is an LLM-powered autonomous coding agent built on a simple but powerful premise: **Failures aren't terminal. They're learning signals.** 

Instead of just spitting out code and hoping for the best, this system uses a self-reflective feedback loop to iteratively plan, write, execute, evaluate, and improve its solutions until the task is completely crushed.

---

## ⚙️ How the Magic Happens

Think of it as an AI development squad packed into a single loop:

```text
Task → Planner* → Coder* → Executor → Evaluator
                              │         │
                              │         ├── Pass ── Done
                              │         │
                              └─────────┴── Fail ── Reflector*
                                                      │
                                                      ▼
                                               Retry (Coder)
```
*\* Components currently in skeleton phase.*

1. 🗺️ **Planner**: Breaks down your raw task into a crisp, actionable strategy.
2. 💻 **Coder**: Turns that plan into pythonic reality.
3. ⚡ **Executor**: Throws the code into a sandboxed arena to see if it survives.
4. ⚖️ **Evaluator**: The strict judge. Did the code actually do what we wanted? Powered by **LangChain** and **Groq**.
5. 🔍 **Reflector**: The system's secret weapon. If the code failed, the Reflector analyzes *why* and formulates a brilliant new strategy for the next attempt.
6. 🔁 **Control Loop**: The orchestrator keeping the chaos organized, managing state, and ensuring we don't loop forever.

---

## 📂 Project Architecture

A clean, modular structure designed for scale and understandability:

```text
Reflexion System/
├── main.py                  # The ignition switch (Entry point)
├── config.py                # Centralized command center (Draft)
├── requirements.txt         # Fuel (Dependencies)
├── .env                     # Secrets (Shh!)
├── app/
│   ├── __init__.py
│   ├── control_loop.py      # The heartbeat & iteration logic
│   ├── planner.py           # Task interpretation (Skeleton)
│   ├── coder.py             # Code generation (Skeleton)
│   ├── evaluator.py         # Output evaluation (Groq/LangChain)
│   ├── reflector.py         # Failure analysis (Skeleton)
│   ├── state.py             # Shared immutable state definitions
│   └── prompts/             # LLM orchestration layer
│       ├── executor.py      # Sandboxed execution logic
│       ├── planner_prompt.txt
│       ├── coder_prompt.txt
│       ├── evaluator_prompt.txt
│       └── reflector_prompt.txt
└── tests/
    └── test_tasks.py        # Proving it actually works (Skeleton)
```

---

## 🛠️ Technology Stack

- **Core Logic:** Python 3.10+
- **LLM Orchestration:** [LangChain](https://www.langchain.com/)
- **Compute:** [Groq Cloud](https://groq.com/) (Llama 3 70B)
- **State Management:** Immutable Python Dataclasses

---

## 🚀 Get Started

### Prerequisites

- **Python 3.10+**
- A **Groq API Key** (Get it at [Groq Cloud](https://console.groq.com/))

### Quickstart

```bash
# 1. Grab the code
git clone https://github.com/GitTanish/Reflexion-System.git
cd Reflexion-System

# 2. Forge a virtual environment
python -m venv .venv

# 3. Activate it
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 4. Install the goods
pip install langchain langchain-groq python-dotenv pydantic
```

---

## 🏗️ What's Built So Far

| Component | Status |
| :--- | :--- |
| File structure & scaffolding | 🟢 Done |
| `ReflexionState` (immutable dataclass) | 🟢 Done |
| Control loop | 🟢 Done (Core logic implemented) |
| Evaluator agent | 🟢 Done (Groq/LangChain integration) |
| Planner agent | 🔴 Skeleton only |
| Coder agent | 🔴 Skeleton only |
| Executor (sandboxed runner) | 🟢 Done |
| Reflector agent | 🔴 Skeleton only |
| Prompt templates | 🟡 Skeletons created |
| Config / env loading | 🟡 Initialized in `main.py` |
| Entry point (`main.py`) | 🟡 Initialized |
| Tests | 🔴 Skeleton only |

---

## 🧠 Design Philosophy

- **Immutable State:** Our `ReflexionState` is frozen. Every iteration spawns a brand-new state via `dataclasses.replace()`. This ensures a clean history and prevents side effects.
- **Agentic Modularization:** Each phase (Planner, Coder, Evaluator) is a decoupled module, making it easy to swap LLMs or logic specific to that role.
- **Fail-Fast Loop:** The system is built to embrace failure as the primary driver for improvement.

---

## 📜 License

MIT - See the LICENSE file for details.
