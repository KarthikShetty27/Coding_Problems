# Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
#
# Note: If at any instance, there are no more subarrays of size greater than or equal to K,
# then reverse the last subarray (irrespective of its size).
# You shouldn't return any array, modify the given array in-place.

# Example 1:
# Input:
# N = 5, K = 3
# arr[] = {1,2,3,4,5}
# Output: 3 2 1 5 4
# Explanation: First group consists of elements
# 1, 2, 3. Second group consists of 4,5.

# Your Task:
# You don't need to read input or print anything.
# The task is to complete the function reverseInGroups() which takes the array,
# N and K as input parameters and modifies the array in-place.


def reverseInGroups(arr, k, n):
    for i in range(0, n, k):
        left = i
        right = min(i + k - 1, n - 1)
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    print(arr)


n = 5
k = 3
arr = [1, 2, 3, 4, 5]
reverseInGroups(arr, k, n)
