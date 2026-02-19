# evaluator.py

from dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel, Field
from state import ReflexionState

from langchain_groq import ChatGroq
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate


# -------- Failure Type Enum --------
class FailureType(str, Enum):
    SYNTAX_ERROR = "syntax_error"
    RUNTIME_ERROR = "runtime_error"
    LOGIC_ERROR = "logic_error"
    SPEC_MISMATCH = "spec_mismatch"
    NO_ERROR = "no_error"


# -------- Internal Domain Model --------
@dataclass
class EvaluationResult:
    failure_type: FailureType
    reasoning: str
    confidence: float


# -------- LLM Output Schema --------
class LLMOutputModel(BaseModel):
    failure_type: FailureType = Field(
        description="Type of failure detected"
    )
    reasoning: str = Field(
        description="Short explanation of why this failure type was chosen"
    )
    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1"
    )


# -------- Model Instantiation (Module Level) --------
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0
)

parser = PydanticOutputParser(pydantic_object=LLMOutputModel)

prompt = ChatPromptTemplate.from_template(
    """
You are a strict evaluation engine for a coding agent.

Original Task:
{original_task}

Agent Interpretation:
{interpreted_task}

Generated Code:
{current_code}

Execution Output:
{execution_output}

Error Log:
{error_log}

Classify the result strictly into one failure_type.
Provide reasoning.
Provide confidence between 0 and 1.

{format_instructions}
"""
)


# -------- Evaluation Function --------
def evaluate(state: ReflexionState) -> EvaluationResult:
    try:
        formatted_prompt = prompt.format(
            original_task=state.original_task,
            interpreted_task=state.interpreted_task,
            current_code=state.current_code,
            execution_output=state.execution_output,
            error_log=state.error_log,
            format_instructions=parser.get_format_instructions()
        )

        response = llm.invoke(formatted_prompt)

        parsed = parser.parse(response.content)

        return EvaluationResult(
            failure_type=parsed.failure_type,
            reasoning=parsed.reasoning,
            confidence=parsed.confidence
        )

    except Exception as e:
        return EvaluationResult(
            failure_type=FailureType.LOGIC_ERROR,
            reasoning=f"Evaluation failed: {str(e)}",
            confidence=0.2
        )
