"""Program 009: Min-Heap Implementation from scratch."""
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("pop from empty heap")
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return root

    def _sift_up(self, idx: int):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx: int):
        n = len(self.heap)
        while True:
            smallest = idx
            l = 2 * idx + 1
            r = 2 * idx + 2
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest != idx:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break

if __name__ == "__main__":
    print("--- 009: Min Heap ---")
    h = MinHeap()
    for val in [15, 10, 20, 17, 8, 25]:
        h.push(val)
    sorted_out = [h.pop() for _ in range(6)]
    print(f"Extracted elements in min order: {sorted_out}")
