#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidBlock(board) and self.isValidRowCol(board)

    def isValidRowCol(self, board):
        col = dict()
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != '.':
                    col[j] = col.get(j, set())
                    if board[i][j] in row or board[i][j] in col[j]:
                        return False
                    row.add(board[i][j])
                    col[j].add(board[i][j])
        return True   
    
    def isValidBlock(self, board):
        col = dict()
        for i in range(3):
            for j in range(3):
                tmp = [board[l][m] for l in range(i*3,i*3+3) \
                    for m in range(j*3,j*3+3) if board[l][m] != '.']
                if len(tmp) != len(set(tmp)):
                    return False
        return True

