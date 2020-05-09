# https://leetcode.com/problems/majority-element/

from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num]  > len(nums) // 2:
                return num
        
        return -1

s = Solution()
assert s.majorityElement([3,2,3]) == 3
assert s.majorityElement([2,2,1,1,1,2,2]) == 2