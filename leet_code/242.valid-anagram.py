#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (52.05%)
# Likes:    695
# Dislikes: 102
# Total Accepted:    338.1K
# Total Submissions: 648.5K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        
        tmp = [0]*26
        if len(s) != len(t): return False
        
        for c1,c2 in zip(s,t):
            tmp[ord(c1)-ord('a')] += 1
            tmp[ord(c2)-ord('a')] -= 1
        for i in tmp:
            if i !=0:
                return False
        return True

