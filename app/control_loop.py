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

def initialize_state(task:str) -> ReflexionState:
    return ReflexionState(
        original_task=task,
        interpreted_task="",
        plan="",
        current_code="",
        execution_output="",
        error_log="",
        retry_count=0,
        current_strategy="",
        strategy_history=[],
        failure_history=[],
        status="running"
    )

MAX_RETRIES = 3
def run_reflexion_loop(task:str):
    state = initialize_state(task)
    
    while state.status == 'running':
        print(f"Iteration: {state.retry_count}")

        # simulate evaluator result
        failure_type = 'logic_error'

        new_retry = state.retry_count +1

        new_failure_history = state.failure_history + [failure_type]

        # decide new status
        if new_retry >= MAX_RETRIES:
            new_status = 'terminated'
        else:
            new_status = 'running'

        state = replace(
            state,
            retry_count= new_retry,
            failure_history = new_failure_history,
            status = new_status
        )
    return state


if __name__ == "__main__":
    final_state = run_reflexion_loop("write a function to add two numbers")
    print(final_state)
    