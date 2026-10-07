"""Program 008: Trie (Prefix Tree) for Autocomplete and Fast Lookup."""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_end_of_word

    def autocomplete(self, prefix: str) -> list[str]:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]
        
        words = []
        def dfs(node, path):
            if node.is_end_of_word:
                words.append(prefix + path)
            for ch, child in node.children.items():
                dfs(child, path + ch)
        dfs(curr, "")
        return words

if __name__ == "__main__":
    print("--- 008: Trie Prefix Tree ---")
    trie = Trie()
    for w in ["apple", "app", "application", "apt", "banana", "band"]:
        trie.insert(w)
    print(f"Search 'app': {trie.search('app')}")
    print(f"Autocomplete 'ap': {trie.autocomplete('ap')}")
    print(f"Autocomplete 'ba': {trie.autocomplete('ba')}")
