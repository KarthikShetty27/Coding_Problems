# You will be given an array arr of integers of length N.
# You can construct an integer from two integers by treating the integers as strings and then concatenating them.
# For example, 19 and 4 can be used to construct 194 and 419.
# The task is to find whether it’s possible to construct an integer using all the digits of the numbers such that
# it would be divisible by 3.
# If it is possible then print 1 and if not print 0

# For example:
# INPUT:
# N=2
# arr={1, 4}
# OUTPUT:
# 0

def is_divisible_by_3(arr):
    # Calculate the sum of all elements in the array
    total_sum = sum(arr)

    # Check if the sum is divisible by 3
    if total_sum % 3 == 0:
        return 1
    else:
        return 0

# Input
N = int(input("Enter the number of elements: "))
arr = [int(x) for x in input("Enter the array elements separated by spaces: ").split()]

# Call the function to check if it's possible to construct a divisible integer
result = is_divisible_by_3(arr)

# Print the result
print(result)
