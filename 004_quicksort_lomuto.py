"""Program 004: In-Place QuickSort with Lomuto Partition Scheme."""
def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr: list[int], low: int, high: int):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

if __name__ == "__main__":
    print("--- 004: QuickSort Lomuto ---")
    data = [64, 34, 25, 12, 22, 11, 90, 45, 1]
    print(f"Original: {data}")
    quicksort(data, 0, len(data) - 1)
    print(f"Sorted:   {data}")
