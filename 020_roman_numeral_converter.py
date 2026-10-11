"""Program 020: Roman Numeral to Integer & Integer to Roman Numeral."""
VAL_MAP = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

def int_to_roman(num: int) -> str:
    res = []
    for val, sym in VAL_MAP:
        while num >= val:
            res.append(sym)
            num -= val
    return "".join(res)

def roman_to_int(s: str) -> int:
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    n = len(s)
    for i in range(n):
        val = symbols[s[i]]
        if i + 1 < n and val < symbols[s[i + 1]]:
            total -= val
        else:
            total += val
    return total

if __name__ == "__main__":
    print("--- 020: Roman Numeral Converter ---")
    years = [1984, 2026, 44]
    for y in years:
        rom = int_to_roman(y)
        back = roman_to_int(rom)
        print(f"{y} -> {rom} -> {back}")
