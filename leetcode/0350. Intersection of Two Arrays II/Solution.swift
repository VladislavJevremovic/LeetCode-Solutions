// https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution {
    func intersect(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let nums1 = nums1.sorted()
        let nums2 = nums2.sorted()

        var i = 0, j = 0
        var r = [Int]()
        while i < nums1.count && j < nums2.count {
            if nums1[i] < nums2[j] {
                i += 1
            } else if nums1[i] > nums2[j] {
                j += 1
            } else {
                r.append(nums1[i])
                i += 1
                j += 1
            }
        }

        return r
    }
}

let s = Solution()
assert(s.intersect([1,2,2,1], [2,2]).sorted() == [2,2])
assert(s.intersect([4,9,5], [9,4,9,8,4]).sorted() == [4,9])
