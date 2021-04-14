#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            if cur_sum > 0:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            ans = max(ans, cur_sum)
        return ans
# @lc code=end

