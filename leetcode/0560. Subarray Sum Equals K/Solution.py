# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c, s = 0, 0
        m = collections.defaultdict(int)
        m[0] = 1
        for i, num in enumerate(nums):
            s += num
            if (s - k) in m:
                c += m[s - k]
            m[s] = m[s] + 1
            
        return c

s = Solution()
assert s.subarraySum([1,1,1], 2) == 2