// https://leetcode.com/problems/flipping-an-image

class Solution {
    func flipAndInvertImage(_ A: [[Int]]) -> [[Int]] {
        var result = [[Int]]()
        let n = A.count

        for row in A {
            var new_row = [Int]()
            for j in 0..<n {
                new_row.append(1 - row[n - j - 1])
            }
            result.append(new_row)
        }

        return result
    }
}