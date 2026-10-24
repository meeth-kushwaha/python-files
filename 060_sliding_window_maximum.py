"""Program 060: Sliding Window Maximum using Monotonic Deque."""
from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()
    result = []
    for i, num in enumerate(nums):
        # Remove elements outside current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove elements smaller than current
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

if __name__ == "__main__":
    print("--- 060: Sliding Window Maximum ---")
    data = [1, 3, -1, -3, 5, 3, 6, 7]
    window = 3
    print(f"Data: {data}, Window: {window}")
    print("Max in each window:", max_sliding_window(data, window))
