"""Program 066: Arbitrary Number Base Converter (Base 2 - 36)."""
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def int_to_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    digits = []
    sign = "-" if n < 0 else ""
    n = abs(n)
    while n:
        digits.append(DIGITS[n % base])
        n //= base
    return sign + "".join(reversed(digits))

def base_to_int(s: str, base: int) -> int:
    return int(s, base)

if __name__ == "__main__":
    print("--- 066: Base Converter ---")
    val = 255
    print(f"255 in Base 2:  {int_to_base(val, 2)}")
    print(f"255 in Base 16: {int_to_base(val, 16)}")
    print(f"255 in Base 36: {int_to_base(val, 36)}")
