#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(s, path):
            if len(path)==4:
                if not s:
                    res.append('.'.join(path))
                return
            for i in range(1,4):
                if i <= len(s):
                    if i == 1:
                        dfs(s[i:], path+[s[:i]])
                    elif s[0] != '0' and int(s[:i]) < 256:
                        dfs(s[i:], path+[s[:i]])

        dfs(s,[])
        return res

if __name__ == "__main__":
    s = Solution()
    s.restoreIpAddresses("25525511135")
