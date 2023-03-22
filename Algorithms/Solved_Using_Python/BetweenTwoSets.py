----------------------
# Problem Discription:
----------------------

# There will be two arrays of integers. 
# Determine all integers that satisfy the following two conditions:
#  * The elements of the first array are all factors of the integer being considered
#  * The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

----------
# Example:
----------

# Input:
# 2 3
# 2 4
# 16 32 96

# Output:
# 3

-------
# Code:
-------

import math 
import copy
from functools import reduce

def get_lcm(a, b):
    return (a*b)//math.gcd(a, b)

def getTotalX(a, b):
    lcm = reduce(get_lcm, a)
    gcd = reduce(math.gcd, b)
    
    lcm_copy = copy.deepcopy(lcm)
    counter = 0
    
    while lcm_copy <= gcd:
        if gcd % lcm_copy == 0:
            counter += 1
        lcm_copy += lcm
        
    return counter
                
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)
