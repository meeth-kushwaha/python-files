"""Program 090: Coin Change Problem (Minimum Coins & Total Combinations)."""
def min_coins_needed(coins: list[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

def count_ways(coins: list[int], amount: int) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

if __name__ == "__main__":
    print("--- 090: Coin Change Problem ---")
    c = [1, 2, 5]
    amt = 11
    print(f"Coins: {c}, Amount: {amt}")
    print(f"Minimum coins required: {min_coins_needed(c, amt)}")
    print(f"Total distinct ways:    {count_ways(c, amt)}")
