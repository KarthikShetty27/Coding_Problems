# Question:
# You are given a string as input.
# Find the biggest two number pair that is present in the string.

# Example-01:
# Input:
# string = "5268971"

# Output:
# 97

# Code:
def find_largest_two_number_pair(s):
    largest_pair = ""
    for i in range(len(s) - 1):
        current_pair = s[i:i+2]
        if len(current_pair) == 2 and current_pair.isdigit() and current_pair > largest_pair:
            largest_pair = current_pair
    return largest_pair

# Example input
input_string = "254987"
print("The largest two-number pair is:", find_largest_two_number_pair(input_string))

input = ("Enter the string: ")
a = "5268971"
find_biggest_pair(a)
