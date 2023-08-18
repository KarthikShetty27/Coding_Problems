# Question:
# Given an array Q[] of i numbers and another number z,
# the task is to check whether there exist two elements in Q[] whose sum is exactly z.

# Example-01:
# Input: Q[] = {0, -1, 2, -3, 1}, z= -2
# Output: Yes
# Explanation:  If we calculate the sum of the output,1 + (-3) = -2

# Code:
def has_pair_with_sum(arr, x):
    seen = set()
    for num in arr:
        complement = x - num
        if complement in seen:
            return True
        seen.add(num)

    return False

# Example usage
arr = [1, 4, 6, 8, 10, 15]
x = 16

if has_pair_with_sum(arr, x):
    print("Yes, there are two or more elements with sum greater than or equal to", x)
else:
    print("No, there are no two or more elements with sum greater than or equal to", x)
