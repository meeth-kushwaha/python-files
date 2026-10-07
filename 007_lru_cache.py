"""Program 007: Least Recently Used (LRU) Cache using Doubly Linked List & Hash Map."""
class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def _insert(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

if __name__ == "__main__":
    print("--- 007: LRU Cache ---")
    cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(2, 200)
    print(f"Get 1: {cache.get(1)}")
    cache.put(3, 300) # Evicts key 2
    print(f"Get 2: {cache.get(2)} (evicted)")
    print(f"Get 3: {cache.get(3)}")
