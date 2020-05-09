# https://leetcode.com/problems/coin-change/

from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1) # +1 coin, value of which is in [coin, amount]
        
        return dp[amount] if dp[amount] != math.inf else -1

s = Solution()
assert s.coinChange([1, 2, 5], 11) == 3
assert s.coinChange([2], 3) == -1