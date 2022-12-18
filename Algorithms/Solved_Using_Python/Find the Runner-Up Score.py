----------------------
# Problem Discription:
----------------------

# Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given `n` scores. Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains n.
# The second line contains an array A[] of n integers each separated by a space.

----------
# Example:
----------

# Input:
# 5
# 2 3 6 6 5

# Output:
# 5

-------
# Code:
-------

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max_value = max(arr)
    s = -99999
    for i in range(n):
        if arr[i] < max_value and arr[i] > s:
            s = arr[i]
    print(s)
