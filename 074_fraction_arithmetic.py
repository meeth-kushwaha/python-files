"""Program 074: Exact Rational Fraction Arithmetic with GCD."""
import math

class Fraction:
    def __init__(self, num: int, den: int = 1):
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        common = math.gcd(num, den)
        self.num = (num // common) * (-1 if den < 0 else 1)
        self.den = abs(den // common)

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __repr__(self):
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)

if __name__ == "__main__":
    print("--- 074: Fraction Arithmetic ---")
    f1 = Fraction(1, 3)
    f2 = Fraction(1, 6)
    print(f"{f1} + {f2} = {f1 + f2}")
    print(f"{f1} * {f2} = {f1 * f2}")
