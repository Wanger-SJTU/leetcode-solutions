#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:],path+[s[:i]])
        dfs(s, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
