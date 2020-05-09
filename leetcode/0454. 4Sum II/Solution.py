# https://leetcode.com/problems/4sum-ii/

from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        r = 0
        m = defaultdict(int)
        for a in A:
            for b in B:
                m[a + b] += 1
        for c in C:
            for d in D:
                diff = -(c + d)
                if diff in m:
                    r += m[diff]

        return r

s = Solution()
assert s.fourSumCount([1, 2], [-2,-1], [-1, 2], [0, 2]) == 2