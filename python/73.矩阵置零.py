#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n

