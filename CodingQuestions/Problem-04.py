# Question:
# You are given a word and a jumbled word as input.
# Your task is to determine whether the jumbled word can be rearranged to form the original word.
# If it is possible to rearrange the letters to match the original word, output 1. Otherwise, output 0.

# Example-01:
# Input:
    # original = "listen"
    # jumbled = "silent"
# Output:
    # 1

# Code:
def rearranged(original, word):
        return sorted(original) == sorted(word)

original_word = input("Enter the ORIGINAL word: ").strip()
input_word = input("Enter the word to check: ").strip()

if rearranged(original_word, input_word):
    print("1 : IT CAN BE REARRANGED")
else:
    print("0 : IT CAN NOT BE REARRANGED")