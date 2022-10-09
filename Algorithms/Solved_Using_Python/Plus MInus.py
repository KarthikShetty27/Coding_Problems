----------------------
# Problem Discription:
----------------------

# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.

----------
# Example:
----------

# arr = [1, 1, 0, -1, -1]
# There are n = 5 elements, two positive, two negative and one zero.
# Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000.
# Results are printed as:
# 0.400000 
# 0.400000
# 0.200000

-------
# Code:
-------

def plusMinus(arr):
    positive = 0
    negetive = 0
    zero = 0

    for i in range (len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0 :
            negetive +=1
        else:
            zero += 1

    print("%f"%(positive / len(arr)))
    print("%f"%(negetive / len(arr)))
    print("%f"%(zero / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
