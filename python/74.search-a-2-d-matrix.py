#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        rows,cols = len(matrix), len(matrix[0])
        low,high = 0, rows*cols -1

        while low <=high:
            mid = (low+high)//2
            num = matrix[mid//cols][mid%cols]
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

       

