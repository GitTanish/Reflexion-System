from state import ReflexionState
from dataclasses import replace
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
import os

# -------- LLM Output Schema --------
class ReflectionOutput(BaseModel):
    new_strategy: str = Field(description="A concise strategy for the next attempt")
    new_plan: str = Field(description="A detailed step-by-step plan reflecting the learned strategy")

# -------- Model Instantiation --------
llm = ChatGroq(
    model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"),
    temperature=0.1
)

parser = PydanticOutputParser(pydantic_object=ReflectionOutput)

reflection_prompt = ChatPromptTemplate.from_template(
    """
You are a reflection engine for a coding agent. Your goal is to analyze failures and suggest a better approach.

Original Task: {original_task}
Current Code:
{current_code}

Execution Output:
{execution_output}

Error Log:
{error_log}

Previous Strategy History:
{strategy_history}

Analyze exactly what went wrong. Was it a syntax error, a logic error, or a misunderstanding of the task?
Provide a new, refined strategy and a specific plan to fix the issue.

{format_instructions}
    """
)

def reflect(state: ReflexionState) -> ReflexionState:
    """
    Analyze the execution failure and generate a new strategy and plan.
    """
    history_str = "\n".join(state.strategy_history) if state.strategy_history else "Initial attempt."
    
    formatted_prompt = reflection_prompt.format(
        original_task=state.original_task,
        current_code=state.current_code,
        execution_output=state.execution_output,
        error_log=state.error_log,
        strategy_history=history_str,
        format_instructions=parser.get_format_instructions()
    )
    
    response = llm.invoke(formatted_prompt)
    parsed = parser.parse(response.content)
    
    # Update strategy history
    new_strategy_history = state.strategy_history + [parsed.new_strategy]
    
    return replace(
        state, 
        current_strategy=parsed.new_strategy,
        plan=parsed.new_plan,
        strategy_history=new_strategy_history
    )
