"""Program 086: Soundex Phonetic Encoding Algorithm."""
def soundex(name: str) -> str:
    name = name.upper()
    if not name:
        return ""
    code_map = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    encoded = [name[0]]
    prev_code = code_map.get(name[0], "")
    for ch in name[1:]:
        digit = code_map.get(ch, "")
        if digit and digit != prev_code:
            encoded.append(digit)
        prev_code = digit if digit else ""
    return ("".join(encoded) + "000")[:4]

if __name__ == "__main__":
    print("--- 086: Soundex Algorithm ---")
    for name in ["Robert", "Rupert", "Smith", "Smythe"]:
        print(f"{name:10} -> {soundex(name)}")
