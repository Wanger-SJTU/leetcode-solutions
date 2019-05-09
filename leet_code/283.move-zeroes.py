#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last =0
        for idx,item in enumerate(nums):
            if item !=0:
                nums[last], nums[idx] = nums[idx],nums[last]
                last +=1
        

