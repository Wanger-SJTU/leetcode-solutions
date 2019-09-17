class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """
    def splitArray(nums, m):
        left,right = max(nums),sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if self.can_split(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        return right

    def can_split(nums, m, sum):
        cnt,curSum = 1,0
        for i in range(len(nums))
            curSum += nums[i]
            if curSum > sum:
                curSum = nums[i]
                cnt+=1
            if cnt > m:
                return False
        return True
    def splitArrayDP(self, nums, m):
        # write your code here
        n = len(nums)
        sums = [0]*(n+1)
        dp = [[float('inf')*(n+1)] for _ in range(m+1)]
        dp[0][0] = 0
        for i in range(1,n+1):
            sums[i] = sums[i - 1] + nums[i - 1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(i-1, j):
                    val = max(dp[i - 1][k], sums[j] - sums[k])
                    dp[i][j] = min(dp[i][j], val)

        return dp[-1][-1]
