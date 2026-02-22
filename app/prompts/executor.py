import io
import sys
import traceback

from dataclasses import dataclass
from typing import Optional

@dataclass
class ExecutionResult:
    stdout: str
    error: Optional[str]
    success: bool

def execute_code(code: str) -> ExecutionResult:
    # Capture stdout
    captured_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output

    try:
        # Restricted namespace
        local_namespace = {}

        exec(code, {}, local_namespace)

        output = captured_output.getvalue()

        return ExecutionResult(
            stdout=output,
            error=None,
            success=True
        )

    except Exception:
        error_msg = traceback.format_exc()

        return ExecutionResult(
            stdout="",
            error=error_msg,
            success=False
        )

    finally:
        sys.stdout = original_stdout