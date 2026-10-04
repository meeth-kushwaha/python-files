"""Program 001: Fibonacci sequence calculation using memoization and LRU cache."""
import time
from functools import lru_cache

def fib_memo(n: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

@lru_cache(maxsize=128)
def fib_cached(n: int) -> int:
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

if __name__ == "__main__":
    print("--- 001: Fibonacci with Memoization ---")
    start = time.perf_counter()
    res = fib_memo(40)
    dur = (time.perf_counter() - start) * 1000
    print(f"fib_memo(40) = {res} in {dur:.3f} ms")
    
    first_10 = [fib_memo(i) for i in range(10)]
    print(f"First 10 Fibonacci numbers: {first_10}")
