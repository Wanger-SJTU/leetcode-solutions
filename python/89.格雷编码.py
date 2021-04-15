#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        #y X = Y & -Y
        for i in range(1,2**n):
            res.append(res[-1] ^(i&-i))
        return res
