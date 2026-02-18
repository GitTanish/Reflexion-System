from dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel, Field
from state import ReflexionState
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0,
    api_key = os.getenv("GROQ_API_KEY"),
    
)

class FailureType(str, Enum):
    SYNTAX_ERROR = "syntax_error"
    LOGIC_ERROR = "logic_error"
    TIMEOUT = "timeout"
    INCORRECT_OUTPUT = "incorrect_output"
    NO_ERROR = "no_error"
    SPEC_MISMATCH = "spec_mismatch"

@dataclass
class EvaluationResult:
    failure_type: FailureType
    reasoning: str
    confidence: float


class LLMOutputModel(BaseModel):
    failure_type: FailureType = Field(
        description = "Type of failure detected"
    )
    reasoning: str = Field(
        description="Short explanation of why this failure type was chosen"
    )
    confidence: float = Field(
        ge= 0.0,
        le= 1.0,
        description="Confidence score between 0 and 1"
    )
    



def evaluate(state:ReflexionState) -> EvaluationResult:

    return EvaluationResult(
        failure_type = FailureType.LOGIC_ERROR,
        reasoning = "Simulated Failure",
        confidence = 0.6

    )

