"""Program 083: Ring Buffer Stream with Overwrite Policy."""
class OverwritingRingBuffer:
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.count = 0

    def write(self, item: any):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.size
        if self.count < self.size:
            self.count += 1

    def read_all(self) -> list[any]:
        if self.count < self.size:
            return self.buffer[:self.count]
        return [self.buffer[(self.head + i) % self.size] for i in range(self.size)]

if __name__ == "__main__":
    print("--- 083: Ring Buffer Stream ---")
    rb = OverwritingRingBuffer(4)
    for x in [1, 2, 3, 4, 5, 6]:
        rb.write(x)
    print("Last 4 items in chronological order:", rb.read_all())
