#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后K个零
#
class Solution:
    def preimageSizeFZF(self, K: int) -> int:

        def countZero(k):
            res = 0
            while k > 0:
                k = k//5
                res += k
            return res

        lo,hi = 0, 5*(K+1)
        while lo <= hi:
            mid = lo + (hi-lo)//2
            num = countZero(mid)
            if num < K:
                lo = mid+1
            elif num > K:
                hi = mid -1
            else:
                return 5
        return 0
