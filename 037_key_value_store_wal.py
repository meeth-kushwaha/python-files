"""Program 037: Persistent Key-Value Store with Write-Ahead Log (WAL)."""
class KeyValueStoreWAL:
    def __init__(self):
        self.data = {}
        self.wal = []

    def set(self, key: str, value: str):
        self.wal.append(("SET", key, value))
        self.data[key] = value

    def get(self, key: str) -> str | None:
        return self.data.get(key)

    def delete(self, key: str) -> bool:
        if key in self.data:
            self.wal.append(("DEL", key, None))
            del self.data[key]
            return True
        return False

    def replay_wal(self, log_entries: list[tuple[str, str, str | None]]):
        for op, k, v in log_entries:
            if op == "SET":
                self.data[k] = v
            elif op == "DEL" and k in self.data:
                del self.data[k]

if __name__ == "__main__":
    print("--- 037: Key-Value Store with WAL ---")
    db = KeyValueStoreWAL()
    db.set("user:101", "Alice")
    db.set("user:102", "Bob")
    db.delete("user:101")
    print("Current State:", db.data)
    print(f"WAL entries count: {len(db.wal)}")
