"""Program 081: Line-by-Line Unified Diff Generator."""
def simple_diff(text1: str, text2: str) -> list[str]:
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    diff = []
    i = j = 0
    while i < len(lines1) and j < len(lines2):
        if lines1[i] == lines2[j]:
            diff.append(f"  {lines1[i]}")
            i += 1
            j += 1
        elif lines2[j] in lines1[i:]:
            diff.append(f"- {lines1[i]}")
            i += 1
        else:
            diff.append(f"+ {lines2[j]}")
            j += 1
    while i < len(lines1):
        diff.append(f"- {lines1[i]}")
        i += 1
    while j < len(lines2):
        diff.append(f"+ {lines2[j]}")
        j += 1
    return diff

if __name__ == "__main__":
    print("--- 081: Simple Diff Generator ---")
    t1 = "apple\nbanana\ncherry"
    t2 = "apple\nblueberry\ncherry\ndate"
    for line in simple_diff(t1, t2):
        print(line)
