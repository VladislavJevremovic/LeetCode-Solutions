# https://leetcode.com/problems/word-search/

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board: List[List[str]], word: str, visited: List[List[bool]], i: int, j: int, index: int, cache: dict) -> bool:
            if index >= len(word): # found the whole word, trying further not needed
                return True

            if (i, j, index) in cache and cache[(i, j, index)]: # we already searched word[index] at this point
                return cache[(i, j, index)]

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited[i][j]: # out of bounds or found already
                return False

            visited[i][j] = True # searching includes this point, can't repeat
            left, right, up, down = False, False, False, False
            if board[i][j] == word[index]:
                left = dfs(board, word, visited, i, j - 1, index + 1, cache)
                right = dfs(board, word, visited, i, j + 1, index + 1, cache)
                up = dfs(board, word, visited, i - 1, j, index + 1, cache)
                down = dfs(board, word, visited, i + 1, j, index + 1, cache)

            visited[i][j] = False # search done here, reset
            cache[(i, j, index)] = (board[i][j] == word[index]) and (left or right or up or down) # store point results

            return cache[(i, j, index)]

        rows = len(board)
        columns = len(board[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]
        cache = {}
        for i in range(rows):
            for j in range(columns):
                found = False
                if board[i][j] == word[0]:
                    found = dfs(board, word, visited, i, j, 0, cache)
                if found:
                    return True

        return False

s = Solution()
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
assert s.exist(board, "ABCCED") == True
assert s.exist(board, "SEE") == True
assert s.exist(board, "ABCB") == False
