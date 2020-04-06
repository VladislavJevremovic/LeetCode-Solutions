// https://leetcode.com/problems/maximum-subarray/

class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        var running_total = 0
        var result = Int.min
        for num in nums {
            if running_total < 0 {
                running_total = 0
            }
            running_total += num
            result = max(result, running_total)
        }

        return result
    }
}

let s = Solution()
assert(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
