#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dataset={}
        for index in range(len(nums)):
            if (target - nums[index]) in dataset:
                return [index, dataset[(target-nums[index])]]
            else:
                dataset[(nums[index])] = index


