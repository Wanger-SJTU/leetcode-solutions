#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        last = 0
        dp[0] = [sum(grid[0][:i+1]) for i in range(n)]
        for i in range(m):
            dp[i][0] = last + grid[i][0]
            last = dp[i][0]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        
        return dp[-1][-1]

if __name__ == "__main__":
    a = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
        ]
    s = Solution()
    print(s.minPathSum(a))
