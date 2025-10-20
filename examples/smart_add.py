#!/usr/bin/env python3
"""
Example: Smart discovery and notebook addition
Shows how to discover notebook content before adding
"""

import subprocess
import sys
from pathlib import Path

def main():
    # Example notebook URL (replace with actual)
    notebook_url = "https://notebooklm.google.com/notebook/c15c0d27-68d6-47fe-a473-ccf47f89df33?authuser=1"

    skill_dir = Path(__file__).parent.parent

    # Step 1: Discover content
    print("[*] Discovering notebook content...")
    discover_cmd = [
        sys.executable,
        str(skill_dir / "scripts" / "run.py"),
        "ask_question.py",
        "--question", "What topics are covered in this notebook? Provide a brief overview.",
        "--notebook-url", notebook_url
    ]

    result = subprocess.run(discover_cmd)
    if result.returncode != 0:
        print("[!] Discovery failed")
        return 1

    # Step 2: Add to library (based on discovered content)
    print("\n[*] Adding to library with discovered metadata...")
    add_cmd = [
        sys.executable,
        str(skill_dir / "scripts" / "run.py"),
        "notebook_manager.py",
        "add",
        "--url", notebook_url,
        "--name", "Example Research Paper",
        "--description", "Research paper discovered via smart discovery",
        "--topics", "research,academic,paper"
    ]

    result = subprocess.run(add_cmd)
    return result.returncode

if __name__ == "__main__":
    sys.exit(main())