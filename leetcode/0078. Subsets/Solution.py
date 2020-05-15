# https://leetcode.com/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result, 0)
        
        return result

    def dfs(self, nums: List[int], temp: List[int], result: List[int], start_index: int) -> None:
        result.append(temp)
        for i in range(start_index, len(nums)):
            self.dfs(nums, temp + [nums[i]], result, i + 1)

s = Solution()
assert sorted(s.subsets([1, 2, 3]), key=lambda x: len(x)) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]