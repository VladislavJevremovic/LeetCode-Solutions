# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = len(nums)
        result = [1] * c
        
        for i in reversed(range(c - 1)):
            result[i] = result[i + 1] * nums[i + 1]
            
        l = 1
        for i in range(c):
            result[i] = result[i] * l
            l *= nums[i]
        
        return result

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     c = len(nums)
    #     result = [0] * c
        
    #     result[0] = 1
    #     for i in range(1, c):
    #         result[i] = nums[i - 1] * result[i - 1]
        
    #     r = 1
    #     for i in reversed(range(c)):
    #         result[i] = result[i] * r
    #         r *= nums[i]
        
    #     return result

s = Solution()
assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]