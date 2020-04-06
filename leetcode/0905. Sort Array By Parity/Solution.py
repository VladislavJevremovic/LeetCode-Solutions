// https://leetcode.com/problems/sort-array-by-parity

from typing import List

class Solution1:
	def sortArrayByParity(self, A: List[int]) -> List[int]:
		n = len(A)
		result = [None] * n
		a = 0
		b = n - 1
		for c in A:
			if c % 2 == 0:
				result[a] = c
				a += 1
			else:
				result[b] = c
				b -= 1
		
		return result

class Solution2:
	def sortArrayByParity(self, A: List[int]) -> List[int]:
		return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])
