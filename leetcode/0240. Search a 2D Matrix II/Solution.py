# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        x, y = m - 1, 0
        while 0 <= x and y <= n - 1:
            v = matrix[x][y]
            if v > target:
                x -= 1
            elif v < target:
                y += 1
            else:
                return True

        return False

s = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
assert s.searchMatrix(matrix, 5) == True
assert s.searchMatrix(matrix, 20) == False
assert s.searchMatrix([], 0) == False