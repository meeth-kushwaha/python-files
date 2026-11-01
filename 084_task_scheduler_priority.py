"""Program 084: Priority Task Scheduler."""
import heapq

class PriorityScheduler:
    def __init__(self):
        self.pq = []
        self._seq = 0

    def schedule(self, priority: int, name: str, payload: any):
        heapq.heappush(self.pq, (priority, self._seq, name, payload))
        self._seq += 1

    def run_next(self) -> str | None:
        if self.pq:
            priority, _, name, payload = heapq.heappop(self.pq)
            return f"Executed [{name}] (priority {priority}) -> {payload}"
        return None

if __name__ == "__main__":
    print("--- 084: Task Scheduler ---")
    sched = PriorityScheduler()
    sched.schedule(3, "Backup", "Nightly DB backup")
    sched.schedule(1, "Critical Alert", "CPU temp exceeded")
    sched.schedule(2, "Sync", "Cloud storage sync")

    while sched.pq:
        print(sched.run_next())
