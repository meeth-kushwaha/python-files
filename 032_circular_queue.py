"""Program 032: Circular Queue (Ring Buffer) Data Structure."""
class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, val: any) -> bool:
        if self.is_full():
            return False
        self.queue[self.tail] = val
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self) -> any:
        if self.is_empty():
            return None
        val = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return val

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

if __name__ == "__main__":
    print("--- 032: Circular Queue ---")
    cq = CircularQueue(3)
    cq.enqueue("A")
    cq.enqueue("B")
    cq.enqueue("C")
    print(f"Is full: {cq.is_full()}")
    print(f"Dequeue: {cq.dequeue()}")
    cq.enqueue("D")
    items = []
    while not cq.is_empty():
        items.append(cq.dequeue())
    print(f"Remaining drained: {items}")
