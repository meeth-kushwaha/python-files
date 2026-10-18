"""Program 042: Thread-Safe Singleton Pattern."""
import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnectionPool(metaclass=SingletonMeta):
    def __init__(self, pool_size: int = 10):
        self.pool_size = pool_size

if __name__ == "__main__":
    print("--- 042: Singleton Pattern ---")
    s1 = DatabaseConnectionPool(20)
    s2 = DatabaseConnectionPool(50)
    print(f"Same instance: {s1 is s2}")
    print(f"Pool size: {s2.pool_size}")
