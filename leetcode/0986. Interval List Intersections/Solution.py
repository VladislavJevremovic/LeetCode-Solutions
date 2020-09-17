# https://leetcode.com/problems/interval-list-intersections/

from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        r = []
        i = j = 0

        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                r.append([lo, hi])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return r


s = Solution()
assert s.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]) == \
       [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
