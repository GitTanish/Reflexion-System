# executor.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class ExecutionResult:
    stdout: str
    error: Optional[str]
    success: bool