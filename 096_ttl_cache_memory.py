"""Program 096: In-Memory Cache with TTL (Time-To-Live)."""
import time

class TTLCache:
    def __init__(self, default_ttl: float = 60.0):
        self.default_ttl = default_ttl
        self.storage = {}

    def set(self, key: str, val: any, ttl: float | None = None):
        expiry = time.time() + (ttl if ttl is not None else self.default_ttl)
        self.storage[key] = (val, expiry)

    def get(self, key: str) -> any:
        if key not in self.storage:
            return None
        val, expiry = self.storage[key]
        if time.time() > expiry:
            del self.storage[key]
            return None
        return val

    def cleanup(self):
        now = time.time()
        expired = [k for k, (_, exp) in self.storage.items() if now > exp]
        for k in expired:
            del self.storage[k]

if __name__ == "__main__":
    print("--- 096: In-Memory TTL Cache ---")
    cache = TTLCache(default_ttl=0.05)
    cache.set("session_token", "XYZ-12345")
    print("Immediate get:", cache.get("session_token"))
    time.sleep(0.06)
    print("After expiration get:", cache.get("session_token"))
