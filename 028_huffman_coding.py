"""Program 028: Huffman Coding for Lossless Compression."""
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char: str | None, freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text: str) -> tuple[dict[str, str], HuffmanNode]:
    freqs = Counter(text)
    heap = [HuffmanNode(char, count) for char, count in freqs.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        parent = HuffmanNode(None, n1.freq + n2.freq)
        parent.left = n1
        parent.right = n2
        heapq.heappush(heap, parent)

    root = heap[0]
    codes = {}
    def generate_codes(node, prefix):
        if node.char is not None:
            codes[node.char] = prefix or "0"
            return
        if node.left:
            generate_codes(node.left, prefix + "0")
        if node.right:
            generate_codes(node.right, prefix + "1")
    generate_codes(root, "")
    return codes, root

if __name__ == "__main__":
    print("--- 028: Huffman Coding ---")
    data = "this is an example for a huffman tree"
    codes, _ = build_huffman_tree(data)
    encoded = "".join(codes[c] for c in data)
    print(f"Original size: {len(data) * 8} bits")
    print(f"Encoded size:  {len(encoded)} bits")
    print(f"Compression ratio: {len(encoded) / (len(data) * 8):.2%}")
