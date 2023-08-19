# Question:
# Given a list of words followed by two words, the task to find the minimum distance between the given two words
# in the list of words

# Example-01:
# Input:
#     S = { "the", "quick", "brown", "fox", "quick"}
#     word1 = "the"
#     word2 = "fox"
# Output: 3
# Explanation: Minimum distance between the words "the" and "fox" is 3

# Code:
def min_distance(words, word1, word2):
    min_dist = float('inf')
    last_seen = None
    words_list = list(words)  # Convert the set to a list

    for i, word in enumerate(words_list):
        if word == word1 or word == word2:
            if last_seen is not None and words_list[last_seen] != word:
                min_dist = min(min_dist, i - last_seen)
            last_seen = i

    return min_dist

# Example usage
S = { "the", "quick", "brown", "fox", "quick"}
word1 = "the"
word2 = "fox"
result = min_distance(S, word1, word2)
print(result)