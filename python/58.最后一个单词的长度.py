#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = len(s)
        # slow and fast pointers
        slow = -1
        # iterate over trailing spaces
        while slow >= -ls and s[slow] == ' ':
            slow-=1
        fast = slow
        # iterate over last word
        while fast >= -ls and s[fast] != ' ':
            fast-=1
        return slow - fast

