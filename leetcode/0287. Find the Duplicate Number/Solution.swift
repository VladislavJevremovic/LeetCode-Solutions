// https://leetcode.com/problems/find-the-duplicate-number/

class Solution {
    func findDuplicate(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        for i in 1..<nums.count {
            if nums[i] == nums[i-1] {
                return nums[i]
            }
        }

        return -1
    }
}