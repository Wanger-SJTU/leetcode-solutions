#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(nums, path, res):
            if not nums:
                res.append(path)
            for i, num in enumerate(nums):
                helper(nums[:i]+nums[i+1:],path+[num], res)
        res = []
        helper(nums, [], res)
        return res
