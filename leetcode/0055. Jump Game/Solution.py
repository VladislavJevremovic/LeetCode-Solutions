# https://leetcode.com/problems/jump-game

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True

        n = len(nums)
        if n < 2:
            return True
        
        furthest_index = nums[0] # how far can we reach
        for i, num in enumerate(nums):
            if furthest_index <= i and not num:
                return False # can't progress past furthest_index (or i)
     
            furthest_index = max(furthest_index, i + num)
            if furthest_index >= n - 1:
                return True
 
        return False

s = Solution()
assert s.canJump([]) == True
assert s.canJump([0]) == True
assert s.canJump([1]) == True
assert s.canJump([1,2]) == True
assert s.canJump([0,2,3]) == False
assert s.canJump([2,3,1,1,4]) == True
assert s.canJump([3,2,1,0,4]) == False
