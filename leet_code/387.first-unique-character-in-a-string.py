#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (49.94%)
# Likes:    979
# Dislikes: 77
# Total Accepted:    266.6K
# Total Submissions: 533.1K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
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

