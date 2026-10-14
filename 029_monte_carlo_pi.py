"""Program 029: Monte Carlo Estimation of Pi."""
import random
import math

def estimate_pi(num_samples: int) -> tuple[float, float]:
    inside_circle = 0
    for _ in range(num_samples):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            inside_circle += 1
    est = 4.0 * inside_circle / num_samples
    error = abs(est - math.pi)
    return est, error

if __name__ == "__main__":
    print("--- 029: Monte Carlo Pi Estimation ---")
    samples = 100_000
    est, err = estimate_pi(samples)
    print(f"Samples: {samples}")
    print(f"Estimated Pi: {est:.5f}")
    print(f"Actual Pi:    {math.pi:.5f}")
    print(f"Absolute Error: {err:.5f}")
