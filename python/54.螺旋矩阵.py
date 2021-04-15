#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

if __name__ == "__main__":
    l = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    s.spiralOrder(l)