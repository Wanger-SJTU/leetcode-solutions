#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import List
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n+1), k))

    def Iterative(self,n,k):
        res = [[]]
        for _ in range(k):
            res = [[i] + c for c in res 
                for i in range(1, c[0] if c else n+1)]
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.combine(4,2)
    print(res)

