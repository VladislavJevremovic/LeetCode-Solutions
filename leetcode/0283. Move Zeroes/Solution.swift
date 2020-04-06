// https://leetcode.com/problems/move-zeroes/

class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        var lastNonZeroFoundAt = 0, current = 0
        while current < nums.count {
            if nums[current] != 0 {
                nums.swapAt(lastNonZeroFoundAt, current)
                lastNonZeroFoundAt += 1
            }

            current += 1
        }
    }
}

let s = Solution()
var nums = [0, 1, 0, 3, 12]
s.moveZeroes(&nums)
assert(nums == [1, 3, 12, 0, 0])
