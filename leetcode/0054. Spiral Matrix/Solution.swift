// https://leetcode.com/problems/spiral-matrix/

class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        var ans = [Int]()
        if matrix.isEmpty {
            return ans
        }

        var r1 = 0, r2 = matrix.count - 1
        var c1 = 0, c2 = matrix[0].count - 1
        while (r1 <= r2 && c1 <= c2) {
            if c1 <= c2 {
                for c in c1...c2 {
                    ans.append(matrix[r1][c])
                }
            }
            if r1 + 1 <= r2 {
                for r in r1 + 1...r2 {
                    ans.append(matrix[r][c2])
                }
            }
            if r1 < r2 && c1 < c2 {
                if c1 + 1 <= c2 - 1 {
                    for c in (c1 + 1...c2 - 1).reversed() {
                        ans.append(matrix[r2][c])
                    }
                }
                if r1 + 1 <= r2 {
                    for r in (r1 + 1...r2).reversed() {
                        ans.append(matrix[r][c1])
                    }
                }
            }

            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        }

        return ans
    }
}