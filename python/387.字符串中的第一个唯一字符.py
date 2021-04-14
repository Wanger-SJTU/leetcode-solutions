#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
class Solution:
    def firstUniqChar(self, s: str) -> int:
        tmp = [0]*26
        for c in s:
            tmp[ord(c)-ord('a')] += 1
        for idx, c in enumerate(s):
            if tmp[ord(c)-ord('a')] == 1:
                return idx
        return -1

