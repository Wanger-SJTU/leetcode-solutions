#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List
import collections

class Solution:
    def partition(self, s: str) -> List[List[str]]:     
        pal_map = collections.defaultdict(set)
        def expand(s, l, r, pal_map):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pal_map[l].add(r+1)
                l -= 1
                r += 1
        for i in range(len(s)):
            expand(s, i, i, pal_map)
            expand(s, i, i+1, pal_map)

        def dfs(pal_map, s, temp, result, l):
            if l == len(s):
                result.append(temp.copy())
                return
            for r in pal_map[l]:
                temp.append(s[l:r])
                dfs(pal_map, s, temp, result, r)
                temp.pop()
        
        result = []
        dfs(pal_map, s, [], result, 0)
        return result

    def partitionDP(self, s: str) -> List[List[str]]:
        M = []
        for i in range(len(s)):
            M.append([0]*len(s))
        for i in range(len(s)):
            M[i][i] = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                M[i][i+1] = 1
        for delta in range(2, len(s)):
            for i in range(0, len(s)-delta):
                if s[i] == s[i+delta] and M[i+1][i+delta-1] == 1:
                    M[i][i+delta] = 1
        
        solutions = [[[]],[[s[-1]]]]
        for j in range(len(s)-2, -1, -1):
            subsolutions = []
            for x in solutions[-1]:
                subsolutions.append([s[j]] + x)
            for delta in range(1, len(s)-j):
                if M[j][j+delta] == 1:
                    for x in solutions[-1-delta]:
                        subsolutions.append([s[j:j+delta+1]] + x)
            solutions.append(subsolutions)
        return solutions[-1]

    def partitiondfs(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
   
    def isPal(self, s):
        return s == s[::-1]

if __name__ == "__main__":
    s= Solution()
    s.partition("aab")