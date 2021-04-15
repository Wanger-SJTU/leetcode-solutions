#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1 if x != 0 else 0
        x = 1/x if n < 0 else x
        res, n = 1, abs(n)
        while n:
            if n&1:
                res *= x
            x *= x
            n >>= 1
        return res                



