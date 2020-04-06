// https://leetcode.com/problems/island-perimeter/

class Solution {
    func islandPerimeter(_ grid: [[Int]]) -> Int {
        var land = 0, adjacent = 0
        for i in 0..<grid.count {
            for j in 0..<grid[0].count {
                if grid[i][j] == 1 {
                    land += 1
                    if i + 1 < grid.count && grid[i + 1][j] == 1 {
                        adjacent += 1
                    }
                    if j + 1 < grid[0].count && grid[i][j + 1] == 1 {
                        adjacent += 1
                    }
                }
            }
        }
        
        return 4 * land - 2 * adjacent
    }
}