"""Program 005: Merge Sort Algorithm (Divide & Conquer)."""
def mergesort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    print("--- 005: Merge Sort ---")
    sample = [38, 27, 43, 3, 9, 82, 10]
    print(f"Input:  {sample}")
    print(f"Sorted: {mergesort(sample)}")
