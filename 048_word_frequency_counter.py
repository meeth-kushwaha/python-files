"""Program 048: Text Analyzer & Word Frequency Counter."""
import re
from collections import Counter

def analyze_text(text: str) -> dict:
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    counts = Counter(words)
    total_words = len(words)
    unique_words = len(counts)
    top_5 = counts.most_common(5)
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "lexical_diversity": (unique_words / total_words) if total_words else 0.0,
        "top_5": top_5
    }

if __name__ == "__main__":
    print("--- 048: Word Frequency Counter ---")
    sample = "Python is powerful, Python is readable, and Python is versatile."
    stats = analyze_text(sample)
    print(f"Total Words: {stats['total_words']}")
    print(f"Top 5 Frequencies: {stats['top_5']}")
