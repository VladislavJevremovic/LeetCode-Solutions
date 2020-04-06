// https://leetcode.com/problems/sort-colors/

class Solution {
    func sortColors(_ nums: inout [Int]) {
        var r = [Int](repeating: 0, count: 3)
        for n in nums {
            r[n] += 1
        }
        var p = 0
        for (i, c) in r.enumerated() {
            (0..<c).forEach { _ in
                nums[p] = i
                p += 1
            }
        }
    }
}