// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var minPrice = Int.max
        var maxProfit = 0
        for price in prices {
            if price < minPrice {
                minPrice = price
            }
            let profit = price - minPrice
            if profit > maxProfit {
                maxProfit = profit
            }
        }

        return maxProfit
    }
}

let s = Solution()
assert(s.maxProfit([]) == 0)
assert(s.maxProfit([7,1,5,3,6,4]) == 5)
assert(s.maxProfit([7,6,4,3,1]) == 0)
