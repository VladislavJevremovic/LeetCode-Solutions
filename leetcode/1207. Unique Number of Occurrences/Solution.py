# https://leetcode.com/problems/unique-number-of-occurrences

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for n in arr:
            if n not in counts:
                counts[n] = 0
            else:
                counts[n] += 1

        return len(set(counts.values())) == len(counts)

s = Solution()
assert s.uniqueOccurrences([1,2,2,1,1,3]) == True
assert s.uniqueOccurrences([1,2]) == False
assert s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) == True
