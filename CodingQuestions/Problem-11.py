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
