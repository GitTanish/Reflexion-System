from dataclasses import dataclass, replace
from typing import List

@dataclass(frozen =True)
class ReflexionState:
    original_task: str
    interpreted_task: str
    plan: str
    current_code: str
    execution_output: str
    error_log : str
    retry_count: int
    current_strategy: str
    strategy_history: list[str]
    failure_history: list[str]
    status: str = 'running'