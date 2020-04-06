// https://leetcode.com/problems/4sum-ii/

class Solution {
    func fourSumCount(_ A: [Int], _ B: [Int], _ C: [Int], _ D: [Int]) -> Int {
        var r = 0
        var m = [Int: Int]()
        for a in A {
            for b in B {
                m[a + b] = (m[a + b] ?? 0) + 1
            }
        }
        for c in C {
            for d in D {
                if let v = m[-(c + d)] {
                    r += v
                }
            }
        }

        return r
    }
}

let s = Solution()
assert(s.fourSumCount([1, 2], [-2,-1], [-1, 2], [0, 2]) == 2)
