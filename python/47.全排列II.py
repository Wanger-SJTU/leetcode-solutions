#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def helper(nums, path, res):
            if not nums:
                res.append(path)
            for i, num in enumerate(nums):
                if i > 0 and num == nums[i-1]:
                    continue
                helper(nums[:i]+nums[i+1:],path+[num], res)
        nums.sort()
        res = []
        helper(nums, [], res)
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.permuteUnique([1,2,1])
    print(res)
