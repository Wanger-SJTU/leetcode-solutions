#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=zip(*matrix[::-1])
        
        


if __name__ == "__main__":
    s =Solution()
    A = [[1,2,3],
        [4,5,6],
        [7,8,9]]
    s.rotate(A)
    print(A)