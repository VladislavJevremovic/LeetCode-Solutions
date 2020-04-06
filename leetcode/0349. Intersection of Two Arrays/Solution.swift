// https://leetcode.com/problems/intersection-of-two-arrays/

class Solution {
    func intersection(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let nums1 = nums1.sorted()
        let nums2 = nums2.sorted()

        var i = 0, j = 0
        var r = [Int]()
        while i < nums1.count && j < nums2.count {
            let a = nums1[i]
            let b = nums2[j]
            if a < b {
                i += 1
            } else if a > b {
                j += 1
            } else {
                r.append(a)
                while i < nums1.count && nums1[i] == a { i += 1 }
                while j < nums2.count && nums2[j] == b { j += 1 }
            }
        }

        return r
    }
}

let s = Solution()
assert(s.intersection([1,2,2,1], [2,2]).sorted() == [2])
assert(s.intersection([2,2], [1,2,2,1]).sorted() == [2])
assert(s.intersection([4,9,5], [9,4,9,8,4]).sorted() == [4,9])
assert(s.intersection([9,4,9,8,4], [4,9,5]).sorted() == [4,9])
