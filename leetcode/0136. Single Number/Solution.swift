// https://leetcode.com/problems/single-number/

class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        return nums.reduce(0, ^)
    }
}

let s = Solution()
assert(s.singleNumber([2,2,1]) == 1)
assert(s.singleNumber([4,1,2,1,2]) == 4)
