"""Program 019: Collatz Conjecture (3n + 1) Analysis."""
def collatz_sequence(n: int) -> list[int]:
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

if __name__ == "__main__":
    print("--- 019: Collatz Conjecture ---")
    num = 27
    seq = collatz_sequence(num)
    print(f"Starting number: {num}")
    print(f"Sequence length: {len(seq)}")
    print(f"Maximum value:   {max(seq)}")
    print(f"First 10 steps:  {seq[:10]} ... -> 1")
