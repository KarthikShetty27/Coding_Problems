# Given an array arr of size n, the task is to check if the given array can be a level order representation of a Max Heap.

def is_max_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        if arr[i] < arr[2 * i + 1] or (2 * i + 2 < n and arr[i] < arr[2 * i + 2]):
            return False
    return True

arr = [9, 15, 10, 7, 12, 11]
n = len(arr)
if is_max_heap(arr, n):
    print("Output: 1")
else:
    print("Output: 0")


