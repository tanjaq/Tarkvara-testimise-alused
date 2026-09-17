#!/usr/bin/env python3
"""Rebuild every generated page in the course site.

    cd tools && python3 build.py

Writes into the repository root: index.html, lesson-*.html and homework/.
Everything else in the repo — compact/, materials/, images/, README.md —
is maintained by hand and is not touched by this script.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# tpl.py is the shared template and is imported by the others, not run directly.
STEPS = [
    ("l01_04.py", "lessons 1-2"),
    ("l03_05.py", "lessons 3-5"),
    ("l06_08.py", "lessons 6-8"),
    ("l09_10.py", "lessons 9-10"),
    ("l11_13.py", "lessons 11-13"),
    ("bonus.py",  "bonus lessons"),
    ("hw.py",     "homework pages"),
    ("index.py",  "course homepage"),
]

def main():
    failed = []
    for script, what in STEPS:
        print(f"\n--- {what} ({script})")
        r = subprocess.run([sys.executable, script], cwd=HERE)
        if r.returncode != 0:
            failed.append(script)
    if failed:
        print("\nFAILED:", ", ".join(failed))
        return 1
    print("\nAll pages rebuilt.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
