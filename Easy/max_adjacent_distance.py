"""
Given a circular array nums, find the maximum absolute difference between adjacent elements.

"""


class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0 
        n = len(nums)
        for i in range(n):
            diff = abs(nums[i]-nums[(i+1)%n])
            result = max(result,diff)
        return result

            

sol= Solution()
nums = [-5,-10,-5]
result = sol.maxAdjacentDistance(nums)

print(result)