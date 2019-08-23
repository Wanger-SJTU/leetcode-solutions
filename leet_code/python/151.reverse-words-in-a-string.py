#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

