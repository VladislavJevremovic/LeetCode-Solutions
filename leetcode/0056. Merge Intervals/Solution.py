# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]: # [..1.[.].2..]
                intervals[i - 1][0] = min(intervals[i][0], intervals[i - 1][0])
                intervals[i - 1][1] = max(intervals[i][1], intervals[i - 1][1])
                
                intervals.pop(i)
            else: # [..1..] [..2..]
                i += 1

        return intervals

s = Solution()
assert s.merge([]) == []
assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert s.merge([[1,4],[4,5]]) == [[1,5]]