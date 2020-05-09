# https://leetcode.com/problems/valid-sudoku/

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxs = [[[] for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                v = board[i][j]
                if v == ".":
                    continue
                
                if v in rows[i]:
                    return False
                else:
                    rows[i].append(v)
                
                if v in cols[j]:
                    return False
                else:
                    cols[j].append(v)

                ii = i // 3
                jj = j // 3
                if v in boxs[ii][jj]:
                    return False
                else:
                    boxs[ii][jj].append(v)
        
        return True

s = Solution()
assert s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) == True
assert s.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) == False
