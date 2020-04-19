# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        c = len(nums)
        if not c:
            return -1

        l = 0
        r = c - 1
        
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        # s = start of right segment
        s = l
        l = 0
        r = c - 1

        if target >= nums[s] and target <= nums[r]:
            l = s # right segment
        else:
            r = s # left segment

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

s = Solution()
assert s.search(None, 0) == -1
assert s.search([], 0) == -1
assert s.search([1], 1) == 0
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1
