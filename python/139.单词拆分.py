#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (35.22%)
# Likes:    2153
# Dislikes: 119
# Total Accepted:    334.6K
# Total Submissions: 949K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # time limited
        def _break(s, words, start):
            if start == len(s): return True
            for i in range(start+1, len(s)+1):
                subStr = s[start:i]
                if subStr in words and _break(s, words, i):
                    return True
            return False
        
        def _wordBreak(s, words, start, mem):
            if start == len(s):
                return True 
            if start in mem:
                return False

            for i in range(start + 1, len(s) + 1):
                if i in mem:
                    continue 
                sub = s[start:i]
                if sub in words and _wordBreak(s, words, i, mem):
                    return True

            mem.add(start)
            return False

        # return _wordBreak(s, set(wordDict), 0, set())
        return self.wordBreakDP(s, wordDict)
    
    def wordBreakDP(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0 and len(wordDict) == 0:
            return True
        if len(s) == 0 or len(wordDict) == 0:
            return False
        wordDict = set(wordDict)
        dict_len = max((len(v)) for v in wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(max(i - dict_len, 0), i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
