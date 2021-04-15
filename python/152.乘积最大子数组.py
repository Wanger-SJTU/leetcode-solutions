#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i_max,i_min = 1,1
        res = -float('inf')
        for num in nums:
            i_max,i_min = (i_max,i_min) if num > 0 else( i_min, i_max)
            i_max = max(i_max * num, num)
            i_min = min(i_min * num, num)
            res = max(i_max, res)
        return res
