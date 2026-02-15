from dataclasses import dataclass, field
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
    strategy_history: List[str] = field(default_factory=list)
    failure_history: List[str] = field(default_factory=list)
    status: str = 'running'