class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1] = [1 for _ in range(n+1)]
        for i in range(1,m+1):
            dp[i][1] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                tmp = dp[i-1][j]+dp[i][j-1]
                dp[i][j]= tmp
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3,2))