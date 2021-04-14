#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# num     result          X   (Y&-Y)               Y
#  0      0 0 0         0 0 1 (1)          0 0 1 (1)
#  1      0 0 1         0 1 0 (2)          0 1 0 (2)
#  2      0 1 1         0 0 1 (1)          0 1 1 (3)
#  3      0 1 0         1 0 0 (4)          1 0 0 (4)
#  4      1 1 0         0 0 1 (1)          1 0 1 (5)
#  5      1 1 1         0 1 0 (2)          1 1 0 (6)
#  6      1 0 1         0 0 1 (1)          1 1 1 (7)
#  7      1 0 0
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        # X = Y & -Y
        for i in range(1,2**n):
            res.append(res[-1] ^(i&-i))
        return res
