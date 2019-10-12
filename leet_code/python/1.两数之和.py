#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dataset={}
        for index in range(len(nums)):
            if (target - nums[index]) in dataset:
                return [index, dataset[(target-nums[index])]]
            else:
                dataset[(nums[index])] = index

