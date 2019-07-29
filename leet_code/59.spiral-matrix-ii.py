#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A,lo = [],n*n+1
        while lo > 1:
            lo,hi = lo-len(A), lo
            A = [list(range(lo, hi))]+list(zip(*A[::-1]))
        return A


if __name__ == "__main__":
    s =Solution()
    s.generateMatrix(3)
    