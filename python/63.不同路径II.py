#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        dp[1][1] = 0 if obstacleGrid[0][0] else 1
        
        for i in range(2, n+1):
            dp[1][i] = 0 if obstacleGrid[0][i-1] else dp[1][i-1]
        for i in range(2, m+1):
            dp[i][1] = 0 if obstacleGrid[i-1][0] else dp[i-1][1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i+1][j+1] = 0 if obstacleGrid[i][j] \
                    else dp[i][j+1] + dp[i+1][j]
        return dp[-1][-1]
        
if __name__ == "__main__":
    a =[[0,0,0],
        [0,1,0],
        [0,0,0]]
    # a=[[0],[0]]
    # a=[[0,1]]
    a=[[0,0],[0,0]]
    s = Solution()
    res = s.uniquePathsWithObstacles(a)
    print(res)

