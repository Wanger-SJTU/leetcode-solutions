#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1,n+1))
        res,k = "",k-1
        while n > 0:
            n-=1
            index,k = divmod(k, math.factorial(n))
            res += str(numbers[index])
            numbers.remove(numbers[index])
        return res

