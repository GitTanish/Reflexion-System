from dataclasses import dataclass, replace
from typing import List
from state import ReflexionState
from evaluator import evaluate



def initialize_state(task:str) -> ReflexionState:
    return ReflexionState(
        original_task=task,
        interpreted_task=task,
        plan="",
        current_code="initial",
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
        result = evaluate(state)

        new_retry = state.retry_count +1

        new_failure_history = state.failure_history + [result.failure_type]

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
    