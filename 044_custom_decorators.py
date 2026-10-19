"""Program 044: Custom Python Decorators (Timing & Retry)."""
import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        print(f"[{func.__name__}] took {duration:.3f} ms")
        return result
    return wrapper

def retry(attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    if i == attempts:
                        raise
                    print(f"Attempt {i} failed: {err}. Retrying...")
        return wrapper
    return decorator

@time_it
def compute_sum(n: int) -> int:
    return sum(range(n))

if __name__ == "__main__":
    print("--- 044: Custom Decorators ---")
    val = compute_sum(100_000)
    print(f"Sum result: {val}")
