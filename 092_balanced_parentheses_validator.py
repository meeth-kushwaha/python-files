"""Program 092: Balanced Multi-Bracket Validator with Error Position."""
def validate_brackets(expression: str) -> tuple[bool, int]:
    bracket_pairs = {')': '(', '}': '{', ']': '[', '>': '<'}
    opening = set(bracket_pairs.values())
    stack = [] # (char, index)

    for idx, ch in enumerate(expression):
        if ch in opening:
            stack.append((ch, idx))
        elif ch in bracket_pairs:
            if not stack or stack[-1][0] != bracket_pairs[ch]:
                return False, idx
            stack.pop()

    if stack:
        return False, stack[-1][1]
    return True, -1

if __name__ == "__main__":
    print("--- 092: Balanced Parentheses Validator ---")
    tests = ["{ [ a + b * ( c - d ) ] }", "( ( [ ] )", "{ [ ] ) }"]
    for expr in tests:
        valid, err_pos = validate_brackets(expr)
        print(f"'{expr}': {'Valid' if valid else f'Error at pos {err_pos}'}")
