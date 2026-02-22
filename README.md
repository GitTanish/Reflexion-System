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

1. 🗺️ **Planner**: Breaks down your raw task into a crisp, actionable strategy.
2. 💻 **Coder**: Turns that plan into pythonic reality.
3. ⚡ **Executor**: Throws the code into a sandboxed arena to see if it survives.
4. ⚖️ **Evaluator**: The strict judge. Did the code actually do what we wanted?
5. 🔍 **Reflector**: The system's secret weapon. If the code failed, the Reflector analyzes *why* and formulates a brilliant new strategy for the next attempt.
6. 🔁 **Control Loop**: The orchestrator keeping the chaos organized, managing state, and ensuring we don't loop forever.

This cycle repeats until the Evaluator is satisfied (Pass!) or we hit our retry limit (`MAX_RETRIES`).

---

## 📂 Project Architecture

A clean, modular structure designed for scale and understandability:

```text
Reflexion System/
├── main.py                  # The ignition switch
├── config.py                # Centralized command center
├── requirements.txt         # Fuel (Dependencies)
├── .env                     # Secrets (Shh!)
├── app/
│   ├── __init__.py
│   ├── control_loop.py      # The heartbeat & immutable ReflexionState
│   ├── planner.py           # Task interpretation
│   ├── coder.py             # Code generation
│   ├── executor_tool.py     # Sandboxed execution
│   ├── evaluator.py         # Output evaluation
│   ├── reflector.py         # Failure analysis
│   ├── state.py             # Shared state definitions
│   └── prompts/             # Where the LLMs get their marching orders
│       ├── planner_prompt.txt
│       ├── coder_prompt.txt
│       ├── evaluator_prompt.txt
│       └── reflector_prompt.txt
└── tests/
    └── test_tasks.py        # Proving it actually works
```

---

## 🚀 Get Started

Ready to take it for a spin? Let's get you set up.

### Prerequisites

- **Python 3.10+**
- An API key for your LLM of choice (OpenAI or Google)

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
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` to `.env` (or just create `.env`) and drop in your keys:

```env
# 🔑 LLM API Keys
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=AIza...

# 🧠 Brain Settings
MODEL_NAME=gpt-4
TEMPERATURE=0.2
MAX_TOKENS=4096

# 🛑 Guardrails
MAX_RETRIES=3
```

---

## 🏗️ What's Built So Far

We're aggressively building this out. Here's where we stand:

| Component | Status |
| :--- | :--- |
| File structure & scaffolding | 🟢 Done |
| `ReflexionState` (immutable dataclass) | 🟢 Done |
| Control loop skeleton | 🟢 Done |
| Evaluator agent | 🟡 Skeleton / Mocked |
| Planner agent | 🔴 Not started |
| Coder agent | 🔴 Not started |
| Executor (sandboxed runner) | 🔴 Not started |
| Reflector agent | 🔴 Not started |
| Prompt templates | 🔴 Not started |
| Config / env loading | 🔴 Not started |
| Entry point (`main.py`) | 🔴 Not started |
| Tests | 🔴 Not started |

---

## 🧠 Why Build It This Way? (Design Philosophy)

- **Immutable State:** Our `ReflexionState` is frozen. Every iteration spawns a brand-new state via `dataclasses.replace()`. Why? It makes tracking history dead-simple and completely eliminates nasty side-effects.
- **Prompt-Driven Agents:** Each phase of the loop (Planner, Coder, etc.) has its own hyper-focused prompt template. We keep instructions pure and separate from the Python logic.
- **Ironclad Budgets:** By strictly enforcing `MAX_RETRIES`, we ensure the system learns efficiently without blowing through your API budget in an infinite loop.

---

## 📜 License

TBD - Check back soon!
