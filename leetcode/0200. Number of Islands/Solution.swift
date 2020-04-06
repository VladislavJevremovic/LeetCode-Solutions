// https://leetcode.com/problems/number-of-islands

class Solution {
  func clearIslandDFS(_ grid: inout [[Character]], _ i: Int, _ j: Int) {
    if grid[i][j] == "1" {
      grid[i][j] = "0"
      if i - 1 >= 0 {
        self.clearIslandDFS(&grid, i - 1, j)
      }
      if i + 1 < grid.count {
        self.clearIslandDFS(&grid, i + 1, j)
      }
      if j - 1 >= 0 {
        self.clearIslandDFS(&grid, i, j - 1)
      }
      if j + 1 < grid[0].count {
        self.clearIslandDFS(&grid, i, j + 1)
      }
    }
  }

  func numIslands(_ grid: [[Character]]) -> Int {
    var r = 0
    var grid = grid

    for i in 0..<grid.count {
      for j in 0..<grid[0].count {
        if grid[i][j] == "1" {
          r += 1
          clearIslandDFS(&grid, i, j)
        }
      }
    }

    return r
  }
}