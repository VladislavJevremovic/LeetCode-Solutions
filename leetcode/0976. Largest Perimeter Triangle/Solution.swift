// https://leetcode.com/problems/largest-perimeter-triangle/

class Solution {
    func largestPerimeter(_ A: [Int]) -> Int {
        let n = A.count
        if n < 3 {
            return 0
        }

        let B = A.sorted()
        var i = n - 3
        while i >= 0 && B[i] + B[i + 1] <= B[i + 2] {
            i -= 1
        }

        return i >= 0 ? B[i] + B[i + 1] + B[i + 2] : 0
    }
}

let s = Solution()
assert(s.largestPerimeter([2,1,2]) == 5)
assert(s.largestPerimeter([1,2,1]) == 0)
assert(s.largestPerimeter([3,2,3,4]) == 10)
assert(s.largestPerimeter([3,6,2,3]) == 8)
