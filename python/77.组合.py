#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def helper(nums, path, res):
            if len(path) == k:
                res.append(path)
            for idx, num in enumerate(nums):
                helper(nums[idx+1:], path+[num], res)
        res = []
        helper(list(range(1,n+1)),[], res)

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4,2))
