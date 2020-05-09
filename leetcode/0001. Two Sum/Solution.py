# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            return []
        
        m = {} # number: index of complement
        for i, num in enumerate(nums):
            c = target - num # complement of num at index i
            if c in m:
                return [m[c], i]
            m[num] = i
            
        return []

s = Solution()
assert s.twoSum([2,7,11,15], 9) == [0, 1]