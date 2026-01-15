"""
Syntax analysis for Python code.
"""

import ast

def check_syntax(file_path: str):
    try:
        with open(file_path, "r") as f:
            source = f.read()
        ast.parse(source)
        return True, "Syntax OK"
    except Exception as e:
        return False, f"Syntax Error: {e}"
