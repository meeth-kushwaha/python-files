"""Program 002: Sieve of Eratosthenes & Prime Factorization."""
def sieve_of_eratosthenes(limit: int) -> list[int]:
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def prime_factors(n: int) -> list[int]:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    print("--- 002: Sieve of Eratosthenes ---")
    primes_up_to_50 = sieve_of_eratosthenes(50)
    print(f"Primes up to 50: {primes_up_to_50}")
    num = 360
    print(f"Prime factors of {num}: {prime_factors(num)}")
