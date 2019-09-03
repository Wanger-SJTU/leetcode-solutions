#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1

        for i,num in enumerate(nums):
            # 如果在 [0,len(nums)-1]的范围内，
            # 并且 num不在 nums 的第 num 个位置
            # 就 交换位置
            while 0 <= num-1 < len(nums) and nums[num-1] != num:
                tmp = num-1
                num, nums[i], nums[tmp] = nums[tmp], nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1


