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

SUCCESS_THRESHOLD = 0.9
MAX_RETRIES = 3

from coder import generate_code
from reflector import reflect

def run_reflexion_loop(task: str):
    state = initialize_state(task)

    while state.status == 'running':
        print(f"Iteration: {state.retry_count}")

        # 1️⃣ Code Generation
        state = generate_code(state)

        # 2️⃣ Execute
        execution_result = execute_code(state.current_code)

        state_after_execution = replace(
            state,
            execution_output=execution_result.stdout,
            error_log=execution_result.error or ""
        )

        # 3️⃣ Evaluate
        evaluation_result = evaluate(state_after_execution)

        # 4️⃣ Success check
        if evaluation_result.failure_type == FailureType.NO_ERROR and evaluation_result.confidence >= SUCCESS_THRESHOLD:
            state = replace(state_after_execution, status="success")
            break

        # 5️⃣ Else: treat as failure -> Reflect
        new_retry = state_after_execution.retry_count + 1

        if new_retry >= MAX_RETRIES:
            new_status = "terminated"
        else:
            new_status = "running"

        state_with_failure = replace(
            state_after_execution,
            retry_count=new_retry,
            failure_history=state_after_execution.failure_history + [evaluation_result.failure_type],
            status=new_status
        )

        # Reflect (only if not terminated)
        if new_status == "running":
            state = reflect(state_with_failure)
        else:
            state = state_with_failure

    return state


if __name__ == "__main__":
    final_state = run_reflexion_loop("write a function to add two numbers")
    print(final_state)
    