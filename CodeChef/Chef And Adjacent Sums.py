----------------------
# Problem Discription:
----------------------

# You are given an array A of size N.
# Consider an array B of size N formed by sorting A in non-decreasing order.
# Let Z=(B(N) + B(N−1)).
# Find whether there exists any rearrangement of the array A, such that, for all (1≤i<N),
# (A(i) + A(i−1)) < Z.
# If such a rearrangement exists, print YES, otherwise print NO.

----------
# Example:
----------

# Sample Input: 
# 4
# 3
# 3 4 4
# 4
# 1 2 3 4
# 2
# 2 2
# 2
# 1 2

# Sample Output:
# YES
# YES
# NO
# NO

-------
# Code:
-------

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # sort the array a in non-decreasing order
    b = sorted(a)
    # calculate the value of Z
    z = b[n-1] + b[n-2]
    # create a new array c to check the condition
    c = [0]*n
    for i in range(n//2):
        c[2*i] = b[n-i-1] # decreasing order of first half of b
        c[2*i+1] = b[i]   # increasing order of second half of b
    # check if the condition is satisfied for all pairs
    flag = True
    for i in range(n-1):
        if c[i] + c[i+1] >= z:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
