"""Program 025: Longest Common Subsequence (LCS) with Backtracking."""
def lcs(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    # Reconstruct string
    chars = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(chars))

if __name__ == "__main__":
    print("--- 025: Longest Common Subsequence ---")
    a = "AGGTAB"
    b = "GXTXAYB"
    res = lcs(a, b)
    print(f"LCS of '{a}' and '{b}': '{res}' (Length: {len(res)})")
