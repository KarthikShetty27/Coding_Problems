----------------------
# Problem Discription:
----------------------

# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

----------
# Example:
----------

# Input: s = "foobar", letter = "o"
  
# Output: 33

# Explanation:
# The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.

-------
# Code:
-------

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return(100 * s.count(letter) // len(s) )
