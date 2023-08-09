# Question: Write a program (WAP) to find the common elements present in the given two strings.
# Example-01:
# Input: a = ["apple", "banana", "orange", "kiwi", "strawberry"]
# Output: result = ""

# Code:
def find_largest_string(string_list):
    largest_string = ""
    for string in string_list:
        if len(string) > len(largest_string):
            largest_string = string
    return largest_string

a = {"Apple", "Banana", "Orange", "Kiwi", "Strawberry"} # list of strings
print(find_largest_string(a))