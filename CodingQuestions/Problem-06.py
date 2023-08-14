# Question:
# WAP To find the minimum number of letters that need to be deleted to make two strings anagrams

# Example-01:
# Input:
# a = "cde"
# b = "abc

# Output:
# 4

# Code:
def find_Anagram(a, b):
    freq_a = {char: a.count(char) for char in set(a)}
    freq_b = {char: b.count(char) for char in set(b)}

    min_del = sum(abs(freq_a.get(char, 0) - freq_b.get(char, 0)) for char in set(a + b))

    return min_del

# Example input
a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
print("The minimum number of letters that need to be deleted are:", find_Anagram(a, b))
