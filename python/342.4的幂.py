#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and num&(num-1)==0 and num&0x55555555 == num
