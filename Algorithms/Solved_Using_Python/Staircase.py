----------------------
# Problem Discription:
----------------------

# Staircase detail
# This is a staircase of size n = 4:

   #
  ##
 ###
####

# * It's base and height are both equal to 'n'.
# * It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
# * Write a program that prints a staircase of size. 

----------
# Example:
----------

# Sample Input:  6 

# Sample Output:

     #
    ##
   ###
  ####
 #####
######


-------
# Code:
-------

def staircase(n):
    for i in range(0, n):
        print(" "*(n-i-1),end='')
        print("#"*(i+1),end='\n') 
                    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
    
