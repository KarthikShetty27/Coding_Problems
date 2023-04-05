----------------------
# Problem Discription:
----------------------

# Chef has an ore with melting point of X degrees.
# Chef’s kiln has a initial temperature of Y degrees. The temperature of the kiln increases by 
# i degrees after the ith minute.
# Find the minimum time in minutes after which the ore starts melting.

----------
# Example:
----------

# Sample Input: 

# 3
# 3 2
# 5 3
# 10 5

# Sample Output:

# 1
# 2
# 3

-------
# Code:
-------

import math

t = int(input())

for z in range(t):
    X, Y = map(int, input().split())

    # calculate the minimum time required for the ore to start melting
    t = math.ceil((math.sqrt(1 + 8*(X-Y)) - 1) / 2)

    print(t)
