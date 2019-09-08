#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend<0) is (divisor <0)
        dividend, divisor = abs(dividend), abs(divisor) 
        res= 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        if not sign:
            res = -res
        return  min(max(-2147483648, res), 2147483647)
# if __name__ == "__main__":
#     s =Solution()
#     s.divide(10,3)