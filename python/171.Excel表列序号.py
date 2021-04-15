#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for idx, char in enumerate(reversed(s)):
            res += 26**(idx)*(ord(char)-ord('A')+1)
        return res

