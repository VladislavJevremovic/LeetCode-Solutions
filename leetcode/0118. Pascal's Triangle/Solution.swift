// https://leetcode.com/problems/pascals-triangle/

class Solution {
    func generate(_ numRows: Int) -> [[Int]] {
        var r = [[Int]]()
        if numRows < 1 { return r }
        for i in 1...numRows {
            var t = [Int]()
            t.append(1)
            if i > 1 {
                let last = r.last ?? []
                if 1 <= i-2 {
                    for j in 1...i-2 {
                        t.append(last[j-1] + last[j])
                    }
                }
                t.append(1)
            }

            r.append(t)
        }

        return r
    }
}