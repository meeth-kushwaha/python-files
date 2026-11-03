"""Program 088: Anagram Grouping with Character Frequency Hash."""
from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for word in words:
        char_count = [0] * 26
        for ch in word.lower():
            if 'a' <= ch <= 'z':
                char_count[ord(ch) - ord('a')] += 1
        groups[tuple(char_count)].append(word)
    return list(groups.values())

if __name__ == "__main__":
    print("--- 088: Group Anagrams ---")
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words))
