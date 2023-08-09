# Question:
# Write a program (WAP) to find a point in a given string such that from that point the sum of LHS = RHS.

# Example-01:
# Input: a = "abcdeedcba"
# Output: result = "abcdeedcba"

# Code:
def find_balance_point(input_string):
    total_sum = sum(ord(char) for char in input_string)
    left_sum = 0

    for index, char in enumerate(input_string):
        if left_sum == total_sum:
            return index-1, char  # Return index and character at the balance point
        total_sum -= ord(char)
        left_sum += ord(char)
    return -1, None  # No balance point found

# Example input string
input_string = "abcdeedcba"

balance_point, char = find_balance_point(input_string)
if balance_point != -1:
    print(f"\n Balance point found after index {balance_point}: '{char}'")
else:
    print("\n No balance point found.")

