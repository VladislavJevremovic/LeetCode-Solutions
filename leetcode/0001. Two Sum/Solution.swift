// https://leetcode.com/problems/two-sum/

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        let n = nums.count
        if n < 2 { return [] }

        var m = [Int: Int]()
        for i in 0..<n {
            let complement = target - nums[i]
            if let x = m[complement] {
                return [x, i]
            }
            m[nums[i]] = i
        }

        return []
    }
}
