# https://leetcode.com/problems/find-peak-element/

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1

        return l

s = Solution()
assert s.findPeakElement([1,2,3,1]) == 2
assert s.findPeakElement([1,2,1,3,5,6,4]) in [1,5]