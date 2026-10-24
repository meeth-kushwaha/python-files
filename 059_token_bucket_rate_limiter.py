"""Program 059: Token Bucket Rate Limiter."""
import time

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = float(capacity)
        self.last_update = time.time()

    def allow_request(self, tokens_needed: int = 1) -> bool:
        now = time.time()
        elapsed = now - self.last_update
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_update = now

        if self.tokens >= tokens_needed:
            self.tokens -= tokens_needed
            return True
        return False

if __name__ == "__main__":
    print("--- 059: Token Bucket Rate Limiter ---")
    limiter = TokenBucket(capacity=3, refill_rate=2.0)
    for i in range(5):
        print(f"Request {i+1}: {'ALLOWED' if limiter.allow_request() else 'REJECTED'}")
