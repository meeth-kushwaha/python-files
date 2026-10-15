"""Program 033: Doubly Linked List with Insertion, Deletion, and Reversal."""
class DLLNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val: int):
        node = DLLNode(val)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def reverse(self):
        curr = self.head
        self.tail = curr
        prev_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            curr.prev = next_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

    def to_list(self) -> list[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

if __name__ == "__main__":
    print("--- 033: Doubly Linked List ---")
    dll = DoublyLinkedList()
    for v in [10, 20, 30, 40]:
        dll.append(v)
    print(f"List forward:  {dll.to_list()}")
    dll.reverse()
    print(f"List reversed: {dll.to_list()}")
