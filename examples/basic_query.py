#!/usr/bin/env python3
"""
Example: Basic query to active notebook
Demonstrates the most common usage pattern
"""

import subprocess
import sys
from pathlib import Path

def main():
    # Get the skill directory
    skill_dir = Path(__file__).parent.parent

    # Run a basic question
    question = "What are the main topics covered in this notebook?"

    cmd = [
        sys.executable,
        str(skill_dir / "scripts" / "run.py"),
        "ask_question.py",
        "--question", question
    ]

    print(f"[*] Asking: {question}")
    result = subprocess.run(cmd)

    return result.returncode

if __name__ == "__main__":
    sys.exit(main())