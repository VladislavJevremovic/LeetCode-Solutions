// https://leetcode.com/problems/coloring-a-border/

class Solution {
    typealias Point = (x: Int, y: Int)

    func colorBorder(_ grid: [[Int]], _ r0: Int, _ c0: Int, _ color: Int) -> [[Int]] {
        var border = [Point]()
        var visited = Array(repeating: Array(repeating: false, count: grid[0].count), count: grid.count)
        var gridv = grid

        dfs(gridv, r0, c0, gridv[r0][c0], &border, &visited)
        for point in border {
            gridv[point.x][point.y] = color
        }

        return gridv
    }

    private func dfs(_ grid: [[Int]], _ i: Int, _ j: Int, _ targetColor: Int, _ border: inout [Point], _ visited: inout [[Bool]]) {
        if i < 0 || j < 0 || i >= grid.count || j >= grid[0].count || visited[i][j] || grid[i][j] != targetColor { return }

        visited[i][j] = true
        if isBorder(grid, i, j, targetColor) {
            border.append((i, j))
        }

        dfs(grid, i - 1, j, targetColor, &border, &visited)
        dfs(grid, i + 1, j, targetColor, &border, &visited)
        dfs(grid, i, j - 1, targetColor, &border, &visited)
        dfs(grid, i, j + 1, targetColor, &border, &visited)
    }

    private func isBorder(_ grid: [[Int]], _ i: Int, _ j: Int, _ targetColor: Int) -> Bool {
        if i == 0 || j == 0 || i == grid.count - 1 || j == grid[0].count - 1 { return true }
        return grid[i - 1][j] != targetColor || grid[i + 1][j] != targetColor || grid[i][j - 1] != targetColor || grid[i][j + 1] != targetColor
    }
}

let s = Solution()
assert(s.colorBorder([[1, 1], [1, 2]], 0, 0, 3) == [[3, 3], [3, 2]])
assert(s.colorBorder([[1, 2, 2], [2, 3, 2]], 0, 1, 3) == [[1, 3, 3], [2, 3, 3]])
assert(s.colorBorder([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2) == [[2, 2, 2], [2, 1, 2], [2, 2, 2]])
