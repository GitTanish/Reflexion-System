from state import ReflexionState
from dataclasses import replace
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# -------- Model Instantiation --------
llm = ChatGroq(
    model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"),
    temperature=0
)

coder_prompt = ChatPromptTemplate.from_template(
    """
You are an expert Python coder. Your task is to write clean, efficient, and correct Python code based on the user's request, plan, and current strategy.

Original Task: {original_task}
Interpreted Task: {interpreted_task}
Current Plan: {plan}
Current Strategy: {current_strategy}

Previous Failures:
{failure_history}

If there were previous failures, analyze them and adjust your code accordingly.
Output ONLY the Python code. Do not include any explanation or markdown formatting like ```python or ```. 
Ensure the code is self-contained and ready to execute.
    """
)

def generate_code(state: ReflexionState) -> ReflexionState:
    """
    Generate or update code based on the current state (task, plan, strategy_history).
    """
    chain = coder_prompt | llm | StrOutputParser()
    
    # Format failure history for the prompt
    history_str = "\n".join(state.failure_history) if state.failure_history else "No previous failures."
    
    new_code = chain.invoke({
        "original_task": state.original_task,
        "interpreted_task": state.interpreted_task,
        "plan": state.plan,
        "current_strategy": state.current_strategy,
        "failure_history": history_str
    })
    
    # Process code to remove potential markdown wrapping if the LLM ignored instructions
    code = new_code.strip()
    if code.startswith("```"):
        lines = code.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        code = "\n".join(lines).strip()

    return replace(state, current_code=code)
