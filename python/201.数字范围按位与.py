#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i+=1
        return n << i

