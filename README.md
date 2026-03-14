# 🧠 Reflexion System: The Autonomous Coding Agent That *Learns* From Its Mistakes

> **🚀 Status: Core Architecture Implemented**
> The foundational modules are live! We've moved beyond scaffolding and now have a functional self-correcting loop.

Ever wish your code could write itself, test itself, and—when it inevitably breaks—*fix* itself? Welcome to the **Reflexion System**.

Inspired by the groundbreaking [Reflexion paper](https://arxiv.org/abs/2303.11366) (Shinn et al., 2023), this is an LLM-powered autonomous coding agent built on a simple but powerful premise: **Failures aren't terminal. They're learning signals.**

Instead of just spitting out code and hoping for the best, this system uses a self-reflective feedback loop to iteratively plan, write, execute, evaluate, and improve its solutions until the task is completely crushed.

---

## ⚙️ How the Magic Happens

Think of it as an AI development squad packed into a single loop:

```text
Task → Coder → Executor → Evaluator
        ^          │         │
        │          │         ├── Pass ── Done
        │          │         │
        └──────────┴─────────┴── Fail ── Reflector
                                          │
                                          ▼
                                   New Plan (Retry)
```

1. 💻 **Coder**: Generates Python code based on the task and current strategy.
2. ⚡ **Executor**: Throws the code into a local environment to capture output and errors.
3. ⚖️ **Evaluator**: The strict judge. Analyzes execution results to classify failures (Syntax, Runtime, Logic, etc.). Powered by **Groq**.
4. 🔍 **Reflector**: The system's secret weapon. If the code failed, the Reflector analyzes *why* and formulates a refined strategy and a new step-by-step plan for the next attempt.
5. 🔁 **Control Loop**: The orchestrator keeping the chaos organized, managing state, and ensuring we don't loop forever.

---

## 📂 Project Architecture

A clean, modular structure designed for scale and understandability:

```text
Reflexion System/
├── main.py                  # The ignition switch (Entry point)
├── config.py                # Configuration management
├── requirements.txt         # Fuel (Dependencies)
├── .env                     # Secrets (Groq API Key)
├── app/
│   ├── __init__.py
│   ├── control_loop.py      # The heartbeat & iteration logic
│   ├── state.py             # Shared immutable state definitions
│   ├── coder.py             # Code generation logic
│   ├── executor.py          # Sandboxed execution engine
│   ├── evaluator.py         # Output evaluation (Groq/LangChain)
│   ├── reflector.py         # Failure analysis & re-planning
│   ├── planner.py           # Initial task interpretation (Skeleton)
│   └── prompts/             # LLM orchestration layer
│       ├── coder_prompt.txt
│       ├── evaluator_prompt.txt
│       ├── planner_prompt.txt
│       └── reflector_prompt.txt
└── tests/
    └── test_tasks.py        # Proving it actually works (Skeleton)
```

---

## 🛠️ Technology Stack

- **Core Logic:** Python 3.10+
- **LLM Orchestration:** [LangChain](https://www.langchain.com/)
- **Compute:** [Groq Cloud](https://groq.com/) (Llama 3.3 70B)
- **Validation:** [Pydantic](https://docs.pydantic.dev/) for structured LLM outputs
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
python -m venv venv

# 3. Activate it
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 4. Install the goods
pip install -r requirements.txt

# 5. Set up your secrets
# Create a .env file and add:
GROQ_API_KEY=your_key_here
MODEL_NAME=llama-3.3-70b-versatile
```

---

## 🏗️ What's Built So Far

| Component | Status |
| :--- | :--- |
| File structure & scaffolding | 🟢 Done |
| `ReflexionState` (immutable dataclass) | 🟢 Done |
| Control loop | 🟢 Done (Core logic implemented) |
| Evaluator agent | 🟢 Done (Groq/LangChain integration) |
| Coder agent | 🟢 Done (Full generation logic) |
| Executor (sandboxed runner) | 🟢 Done |
| Reflector agent | 🟢 Done (Strategy refined & re-planning) |
| Planner agent | 🔴 Skeleton only (Reflector currently handles re-planning) |
| Prompt templates | 🟡 Integrated in-code (Text files are skeletons) |
| Entry point (`main.py`) | 🟢 Done |
| Tests | 🔴 Skeleton only |

---

## 🧠 Design Philosophy

- **Immutable State:** Our `ReflexionState` is frozen. Every iteration spawns a brand-new state via `dataclasses.replace()`. This ensures a clean history and prevents side effects.
- **Agentic Modularization:** Each phase (Coder, Evaluator, Reflector) is a decoupled module, making it easy to swap LLMs or logic specific to that role.
- **Fail-Fast Loop:** The system is built to embrace failure as the primary driver for improvement.

---

## 📜 License

MIT - See the LICENSE file for details.
