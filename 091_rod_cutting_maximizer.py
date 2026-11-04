"""Program 091: Rod Cutting Dynamic Programming Maximizer."""
def rod_cutting(prices: list[int], length: int) -> tuple[int, list[int]]:
    dp = [0] * (length + 1)
    cuts = [0] * (length + 1)

    for i in range(1, length + 1):
        max_val = -1
        for j in range(1, i + 1):
            if j <= len(prices):
                val = prices[j - 1] + dp[i - j]
                if val > max_val:
                    max_val = val
                    cuts[i] = j
        dp[i] = max_val

    # Reconstruct cuts
    pieces = []
    curr = length
    while curr > 0:
        pieces.append(cuts[curr])
        curr -= cuts[curr]
    return dp[length], pieces

if __name__ == "__main__":
    print("--- 091: Rod Cutting Problem ---")
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    rod_len = 8
    best_profit, piece_cuts = rod_cutting(prices, rod_len)
    print(f"Max Profit for length {rod_len}: ${best_profit}")
    print(f"Optimal cut pieces: {piece_cuts}")
