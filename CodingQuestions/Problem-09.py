# Question:
# Given a string in roman no format, task is to convert it to an integer.
# Various symbols and their values are given below.
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000

# Example-01:
# Input: S = V
# Output: 5

# Code:
# num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
#            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
#
# def num2roman(num):
#     roman = ''
#     while num > 0:
#         for i, r in num_map:
#             while num >= i:
#                 roman += r
#                 num -= i
#     return roman
#
# a = input()
# num2roman(a)