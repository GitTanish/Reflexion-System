from dataclasses import dataclass, replace
from typing import List
from state import ReflexionState
from evaluator import evaluate, FailureType
from executor import execute_code



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

        # 1️⃣ Execute
        execution_result = execute_code(state.current_code)

        state_after_execution = replace(
            state,
            execution_output=execution_result.stdout,
            error_log=execution_result.error or ""
        )

        # 2️⃣ Evaluate
        evaluation_result = evaluate(state_after_execution)

        # 3️⃣ If success, terminate
        if evaluation_result.failure_type == FailureType.NO_ERROR:
            state = replace(state_after_execution, status="success")
            break

        # 4️⃣ Reflect (later)
        # For now skip reflection logic

        # 5️⃣ Increment retry
        new_retry = state.retry_count + 1

        # 6️⃣ Check termination
        if new_retry >= MAX_RETRIES:
            new_status = "terminated"
        else:
            new_status = "running"

        state = replace(
            state_after_execution,
            retry_count=new_retry,
            failure_history=state.failure_history + [evaluation_result.failure_type],
            status=new_status
        )
    return state


if __name__ == "__main__":
    final_state = run_reflexion_loop("write a function to add two numbers")
    print(final_state)
    