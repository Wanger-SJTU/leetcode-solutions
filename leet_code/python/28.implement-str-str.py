#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return 0 if len(needle)==0 else -1
        idx = 0
        while idx <= len(haystack)-len(needle):
            j = 0
            while j < len(needle) and haystack[idx] == needle[j]:
                idx,j = idx+1, j+1
            if j == len(needle):
                return idx-j
            idx = idx -j + 1
        return -1

if __name__ == "__main__":
    s =Solution()
    s.strStr("a", "a")
