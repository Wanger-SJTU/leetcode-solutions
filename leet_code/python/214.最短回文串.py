#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

