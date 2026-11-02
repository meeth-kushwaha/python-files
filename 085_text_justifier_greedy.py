"""Program 085: Full Text Justification Formatting."""
def full_justify(words: list[str], max_width: int) -> list[str]:
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > max_width:
            for i in range(max_width - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += " "
            res.append("".join(cur))
            cur, num_of_letters = [], 0
        cur.append(w)
        num_of_letters += len(w)
    return res + [" ".join(cur).ljust(max_width)]

if __name__ == "__main__":
    print("--- 085: Text Justification ---")
    sample_words = ["This", "is", "an", "example", "of", "text", "justification."]
    justified = full_justify(sample_words, 16)
    for line in justified:
        print(f"|{line}|")
