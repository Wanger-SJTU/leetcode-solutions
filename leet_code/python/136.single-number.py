#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = nums[0]
        for num in nums[1:]:
            res = res ^ num
        return res

