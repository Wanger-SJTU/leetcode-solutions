#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
import string
import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        res = []
        if endWord not in wordList:
            return res
        level = {beginWord}
        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        n = node[:i]+char+node[i+1:]
                        if n in wordList and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

