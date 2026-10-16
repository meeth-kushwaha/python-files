"""Program 035: Recursive Descent JSON Parser from Scratch."""
def parse_json(s: str):
    s = s.strip()
    idx = 0

    def parse_value():
        nonlocal idx
        skip_ws()
        if idx >= len(s):
            return None
        ch = s[idx]
        if ch == '"':
            return parse_str()
        elif ch == '{':
            return parse_obj()
        elif ch == '[':
            return parse_arr()
        elif ch in '-0123456789':
            return parse_num()
        elif s.startswith("true", idx):
            idx += 4
            return True
        elif s.startswith("false", idx):
            idx += 5
            return False
        elif s.startswith("null", idx):
            idx += 4
            return None
        raise ValueError(f"Unexpected token at {idx}: {s[idx:]}")

    def skip_ws():
        nonlocal idx
        while idx < len(s) and s[idx] in " \t\r\n":
            idx += 1

    def parse_str():
        nonlocal idx
        idx += 1 # skip '"'
        start = idx
        while idx < len(s) and s[idx] != '"':
            idx += 1
        val = s[start:idx]
        idx += 1 # skip '"'
        return val

    def parse_num():
        nonlocal idx
        start = idx
        while idx < len(s) and (s[idx] in "0123456789.-+eE"):
            idx += 1
        num_str = s[start:idx]
        return float(num_str) if "." in num_str else int(num_str)

    def parse_arr():
        nonlocal idx
        idx += 1 # skip '['
        arr = []
        skip_ws()
        if idx < len(s) and s[idx] == ']':
            idx += 1
            return arr
        while True:
            arr.append(parse_value())
            skip_ws()
            if s[idx] == ',':
                idx += 1
            elif s[idx] == ']':
                idx += 1
                break
        return arr

    def parse_obj():
        nonlocal idx
        idx += 1 # skip '{'
        obj = {}
        skip_ws()
        if idx < len(s) and s[idx] == '}':
            idx += 1
            return obj
        while True:
            skip_ws()
            key = parse_str()
            skip_ws()
            assert s[idx] == ':', f"Expected ':' at {idx}"
            idx += 1
            val = parse_value()
            obj[key] = val
            skip_ws()
            if s[idx] == ',':
                idx += 1
            elif s[idx] == '}':
                idx += 1
                break
        return obj

    return parse_value()

if __name__ == "__main__":
    print("--- 035: Pure Python JSON Parser ---")
    raw = '{"name": "Alice", "age": 30, "scores": [95, 88, 100], "is_admin": true}'
    parsed = parse_json(raw)
    print("Parsed dict:", parsed)
    print("Type check:", type(parsed["scores"]), type(parsed["is_admin"]))
