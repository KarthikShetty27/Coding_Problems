# Question: Write a program (WAP) to find the common elements present in the given two strings.
# Example-01:
# Input: a = "1,2,3,4,5" and b = "9,2,8,4,7,6"
# Output: result = "2,4"

# Code:
a = input("Enter a string 1 : ")
b = input("Enter a string 2 : ")

set_a = set(a.split(","))
set_b = set(b.split(","))

result_string = ','.join(set_a.intersection(set_b))
print(result_string)

# Output:
# Enter a string 1 : 1,2,3,6,9,5
# Enter a string 2 : 1,4,7,8,5,3
# 5, 1, 3