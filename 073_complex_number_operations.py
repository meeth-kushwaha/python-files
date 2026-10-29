"""Program 073: Custom Complex Number Math Class."""
import math

class MyComplex:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return MyComplex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def polar(self) -> tuple[float, float]:
        r = math.hypot(self.real, self.imag)
        theta = math.atan2(self.imag, self.real)
        return r, theta

    def __repr__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"({self.real} {sign} {abs(self.imag)}j)"

if __name__ == "__main__":
    print("--- 073: Complex Number Class ---")
    c1 = MyComplex(3, 4)
    c2 = MyComplex(1, -2)
    print("c1 * c2:", c1 * c2)
    print("Polar coordinates of c1 (r, theta):", c1.polar())
