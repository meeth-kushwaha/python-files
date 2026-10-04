"""Program 003: Binary Search Tree (BST) with Insertion, Search, Traversal, and Deletion."""
class BSTNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key: int):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key: int) -> bool:
        curr = self.root
        while curr:
            if curr.key == key:
                return True
            curr = curr.left if key < curr.key else curr.right
        return False

    def in_order(self) -> list[int]:
        res = []
        def traverse(node):
            if node:
                traverse(node.left)
                res.append(node.key)
                traverse(node.right)
        traverse(self.root)
        return res

if __name__ == "__main__":
    print("--- 003: Binary Search Tree ---")
    bst = BinarySearchTree()
    for val in [50, 30, 20, 40, 70, 60, 80]:
        bst.insert(val)
    print(f"In-order traversal: {bst.in_order()}")
    print(f"Contains 40? {bst.search(40)}")
    print(f"Contains 99? {bst.search(99)}")
