"""Program 018: Quadratic Equation Solver with Complex Roots."""
import cmath

def solve_quadratic(a: float, b: float, c: float) -> tuple[complex, complex]:
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation.")
    discriminant = b**2 - 4*a*c
    sqrt_d = cmath.sqrt(discriminant)
    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)
    return root1, root2

if __name__ == "__main__":
    print("--- 018: Quadratic Equation Solver ---")
    # Equation: x^2 - 5x + 6 = 0
    r1, r2 = solve_quadratic(1, -5, 6)
    print(f"x^2 - 5x + 6 = 0 roots: {r1.real:.2f}, {r2.real:.2f}")
    
    # Equation: x^2 + 4x + 13 = 0 (Complex roots)
    c1, c2 = solve_quadratic(1, 4, 13)
    print(f"x^2 + 4x + 13 = 0 roots: {c1}, {c2}")
