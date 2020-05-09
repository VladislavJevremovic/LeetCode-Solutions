# https://leetcode.com/problems/shuffle-an-array/

from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums 
        self.original = nums[:]

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = self.original[:]
        
        return self.original

    def shuffle(self) -> List[int]:
        n = len(self.array)
        for i in range(n):
            swap_i = random.randrange(i, n)
            self.array[i], self.array[swap_i] = self.array[swap_i], self.array[i]
        
        return self.array

nums = [1,2,3]
s = Solution(nums)
s.shuffle()
assert s.reset() == [1,2,3]