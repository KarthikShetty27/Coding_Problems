# Question:
# Given an integer array nums
# return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Code:
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        # Initialize prefix and suffix arrays
        prefix = [1] * n
        suffix = [1] * n
        # Calculate prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        # Calculate suffix array
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        # Calculate the final answer array
        answer = [prefix[i] * suffix[i] for i in range(n)]

        return answer


# Product Except Self (pes)
pes = Solution()
nums = [2, 9, 2, 7, 2]
result = pes.productExceptSelf(nums)
print(result)