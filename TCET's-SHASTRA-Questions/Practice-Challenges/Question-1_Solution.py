---------------
# Problem-Link: https://www.hackerrank.com/contests/tcet-shastra-long-coding-challenge-practice-1/challenges/l1-h/problem
---------------

----------------------
# Problem Discription:
----------------------

# You are given a task to write a program that can compute the prefix sum of a list of integers.
# A prefix sum of a list is a new list obtained by adding each element of the original list to the sum of all the elements that come before it. 
# For example, the prefix sum of the list [1, 2, 3, 4, 5] is [1, 3, 6, 10, 15].

# Your program should read the list of integers from the standard input and print the prefix sum of the list to the standard output.

----------------------
# Input Format
----------------------

# The first line of input contains an integer  denoting the number of test cases .
# for each t testcase the inputs are:
# * The first line of the input is read as an integer n. This variable represents the number of elements in the list.
# * The second line of the input is read as a list of n integers . These variables represent the elements of the list.

-------
# Example:
-------

# Sample Input:
#   1
#   5
#   12345
  
# Sample Output:
#   1 3 6 10 15

-------
# Code:
-------

t = int(input())
if 1 <= t <= 10000:
    n = int(input())
    a = list(map(int, input().split()))
    res = [sum(a[:i+1]) for i in range(n)]
    for j in res:
        print(j,end=" ")
else:
    print("Error value of t not in range.")
