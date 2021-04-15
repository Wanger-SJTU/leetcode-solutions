#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=zip(*matrix[::-1])
        
        

