// https://leetcode.com/problems/house-robber/submissions/

class Solution {
    func rob(_ nums: [Int]) -> Int {
        var curr = 0, prev = 0

        for i in 0..<nums.count {
            (prev, curr) = (curr, max(curr, prev + nums[i]))
        }

        return curr
    }
}

let s = Solution()
assert(s.rob([1, 2, 3, 1]) == 4)
assert(s.rob([2, 7, 9, 3, 1]) == 12)
