from dotenv import load_dotenv
import sys
import os

load_dotenv()
sys.path.append(os.path.join(os.getcwd(), "app"))

from control_loop import run_reflexion_loop

if __name__ == "__main__":
    task = "Write a Python function to calculate the nth Fibonacci number."
    final_state = run_reflexion_loop(task)
    print("\n--- Final Result ---")
    print(f"Status: {final_state.status}")
    print(f"Code:\n{final_state.current_code}")
