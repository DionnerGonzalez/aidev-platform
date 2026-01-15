"""
Simple style analysis for Python code.
"""

def check_style(file_path: str):
    """
    Checks for basic style issues like line length and trailing whitespace.
    """
    issues = []
    with open(file_path, "r") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, start=1):
        if len(line) > 79:
            issues.append(f"Line {idx}: too long ({len(line)} chars)")
        if line.rstrip() != line.rstrip("\n"):
            issues.append(f"Line {idx}: trailing whitespace")
    if issues:
        return False, "; ".join(issues)
    return True, "Style OK"
