# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = math.inf, 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            
        return max_profit

s = Solution()
assert s.maxProfit([]) == 0
assert s.maxProfit([7,1,5,3,6,4]) == 5
assert s.maxProfit([7,6,4,3,1]) == 0
