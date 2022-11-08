----------------------
# Problem Discription:
----------------------

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

----------
# Example:
----------

# Input:
#   arr = [1,3,5,7,9]
# The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24

# Output:
#   The function prints: 16 24

-------
# Code:
-------

def miniMaxSum(arr):
    
    # Sort the array in ascending order
    arr.sort()

    # Store the sum of the array in the variable = 's'
    s = sum(arr)

    # To get the max value of the array containing five numbers.
    # Subtract the value of first number (arr[0]) from the sum of the array to get the maximum value
    maxResult = s - arr[0]
    
    # To get the min value of the array containing five numbers.
    # Subtract the value of last number (arr[-1]) from the sum of the array to get the mimnimum value
    minResult = s - arr[-1]
    
    # Output
    print(minResult, maxResult)

    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

