class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
        for i in range(1, K + 1):
            for step in range(1, N + 1):
                dp[i][step] = dp[i - 1][step - 1] + (dp[i][step - 1] + 1)
                if dp[K][step] >= N:
                    return step
        return 0
