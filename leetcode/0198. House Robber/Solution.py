# https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for num in nums:
            t = curr
            curr = max(prev + num, curr)
            prev = t
            
        return curr

s = Solution()
assert s.rob([1, 2, 3, 1]) == 4
assert s.rob([2, 7, 9, 3, 1]) == 12
