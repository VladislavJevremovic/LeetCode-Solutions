// https://leetcode.com/problems/max-area-of-island/

class Solution {
    func islandAreaDFS(_ grid: inout [[Int]], _ i: Int, _ j: Int) -> Int {
        var a = 0
        if grid[i][j] == 1 {
            a += 1
            grid[i][j] = 0
            
            if i - 1 >= 0 {
                a += islandAreaDFS(&grid, i - 1, j)
            }
            if i + 1 < grid.count {
                a += islandAreaDFS(&grid, i + 1, j)
            }
            if j - 1 >= 0 {
                a += islandAreaDFS(&grid, i, j - 1)
            }
            if j + 1 < grid[0].count {
                a += islandAreaDFS(&grid, i, j + 1)
            }
        }

        return a
    }

    func maxAreaOfIsland(_ grid: [[Int]]) -> Int {
        var r = 0
        var grid = grid

        for i in 0..<grid.count {
            for j in 0..<grid[0].count {
                if grid[i][j] == 1 {
                    let a = islandAreaDFS(&grid, i, j)
                    r = max(r, a)
                }
            }
        }

        return r
    }
}