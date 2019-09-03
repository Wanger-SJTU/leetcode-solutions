#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#
from functools import reduce
import collections
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        d,N = collections.defaultdict(int), len(words)
        for i in range(N):
            word = words[i]
            for c in word:
                d[word] |= 1 << (ord(c) - ord('a'))
            for j in range(i):
                if not d[words[j]] & d[words[i]]:
                    res = max(res, len(words[j]) * len(words[i]))
        return res


