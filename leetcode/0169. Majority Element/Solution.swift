// https://leetcode.com/problems/majority-element/

class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var d = [Int: Int]()
        for num in nums {
            d[num] = (d[num] ?? 0) + 1
            if (d[num] ?? 0) > nums.count / 2 {
                return num
            }
        }
        
        return -1
    }
}