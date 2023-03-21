----------------------
# Problem Discription:
----------------------

# You are choreographing a circus show with various animals. 
# For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. 
# If it is possible, return YES, otherwise return NO.

----------
# Example:
----------

# Input:
# 0 3 4 2

# Output:
# YES

-------
# Code:
-------

def kangaroo(x1, v1, x2, v2):
        if v1 == v2:
                return "NO"
        else:
                time_to_meet = (x2 - x1) / (v1 - v2)
                if time_to_meet >= 0 and time_to_meet.is_integer():
                        return "YES"
                else:
                        return "NO"

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    
    result = kangaroo(x1, v1, x2, v2)
    print(result)
