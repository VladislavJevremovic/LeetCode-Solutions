// https://leetcode.com/problems/rotate-image/

class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let n = matrix.count
        for i in 0..<n / 2 {
            for j in i..<n - 1 - i {
                let t = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = t
            }
        }
    }
}

let s = Solution()

var m1 = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(&m1)
assert(m1 == [[7,4,1],[8,5,2],[9,6,3]])

var m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(&m2)
assert(m2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
