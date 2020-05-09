# https://leetcode.com/problems/single-number/

from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

s = Solution()
assert s.singleNumber([2,2,1]) == 1
assert s.singleNumber([4,1,2,1,2]) == 4
