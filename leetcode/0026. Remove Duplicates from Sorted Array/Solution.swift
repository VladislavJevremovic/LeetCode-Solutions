// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        if nums.count == 0 { return 0 }

        var i = 0
        for j in 1..<nums.count {
            if nums[j] != nums[i] {
                i += 1
                nums[i] = nums[j]
            }
        }

        return i + 1
    }
}

let s = Solution()

var a1 = [1,1,2]
assert(s.removeDuplicates(&a1) == 2)
assert(a1[..<2] == [1,2])

var a2 = [0,0,1,1,1,2,2,3,3,4]
assert(s.removeDuplicates(&a2) == 5)
assert(a2[..<5] == [0,1,2,3,4])
