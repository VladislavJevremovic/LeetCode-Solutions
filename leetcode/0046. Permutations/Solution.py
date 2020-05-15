# https://leetcode.com/problems/permutations/

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []
        self.permutation(nums, [], result)

        return result

    def permutation(self, nums: List[int], current, result: List[List[int]]) -> None:
        if not nums:
            result.append(current)
            return

        for i in range(len(nums)):
            self.permutation(nums[:i] + nums[(i + 1):], current + [nums[i]], result)

s = Solution()
assert s.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
