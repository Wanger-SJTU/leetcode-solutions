#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for k in zip(*strs):
            if len(set(k))==1:
                res += k[0]
            else:
                break
        return res


if __name__ == "__main__":
    s = ["flower","flow","flight"]
    for k in zip(*s):
        print(k)

