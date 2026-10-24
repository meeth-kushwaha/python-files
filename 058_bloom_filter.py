"""Program 058: Bloom Filter Probabilistic Data Structure."""
import hashlib

class BloomFilter:
    def __init__(self, size: int = 100, num_hashes: int = 3):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item: str) -> list[int]:
        hashes = []
        for i in range(self.num_hashes):
            digest = hashlib.md5(f"{item}-{i}".encode("utf-8")).hexdigest()
            hashes.append(int(digest, 16) % self.size)
        return hashes

    def add(self, item: str):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def contains(self, item: str) -> bool:
        return all(self.bit_array[h] == 1 for h in self._hashes(item))

if __name__ == "__main__":
    print("--- 058: Bloom Filter ---")
    bf = BloomFilter(50, 3)
    bf.add("apple")
    bf.add("banana")
    print("Contains 'apple':", bf.contains("apple"))
    print("Contains 'orange':", bf.contains("orange"))
