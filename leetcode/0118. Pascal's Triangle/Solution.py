# https://leetcode.com/problems/pascals-triangle/

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = []
        if not numRows:
            return r

        for i in range(1, numRows + 1):
            t = []
            t.append(1)
            if i > 1:
                last = r[-1]
                if i >= 3:
                    for j in range(1, (i - 2) + 1):
                        t.append(last[j - 1] + last[j])
                t.append(1)

            r.append(t)

        return r

s = Solution()
assert s.generate(0) == []
assert s.generate(1) == [[1]]
assert s.generate(2) == [[1],[1,1]]
assert s.generate(3) == [[1],[1,1],[1,2,1]]
assert s.generate(4) == [[1],[1,1],[1,2,1],[1,3,3,1]]
assert s.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
