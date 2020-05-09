# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        current_maximum = nums[0]
        maximum = current_maximum
        
        for i in range(1, len(nums)):
            current_maximum = max(current_maximum + nums[i], nums[i])
            maximum = max(maximum, current_maximum)
        
        return maximum

s = Solution()
assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
