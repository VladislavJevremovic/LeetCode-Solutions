// https://leetcode.com/problems/transpose-matrix/

from typing import List

class Solution:
	def transpose(self, A: List[List[int]]) -> List[List[int]]:
		return [[A[i][j] for i in range(len(A))] for j in range(len(A[i]))]