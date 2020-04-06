// https://leetcode.com/problems/coin-change/

class Solution {
    func coinChange(_ coins: [Int], _ amount: Int) -> Int {
        var dp = [Int](repeatElement(amount + 1, count: amount + 1))

        dp[0] = 0
        for coin in coins {
            if coin > amount { continue }
            for i in coin...amount {
                dp[i] = min(dp[i], dp[i - coin] + 1)
            }
        }

        return dp[amount] > amount ? -1 : dp[amount]
    }
}