#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for i,num in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)

            for j in range(len(res)-l, len(res)):
                res.append(res[j]+[num])
        return sorted(res)

if __name__ == "__main__":
    s = Solution()
    res = s.subsetsWithDup([4,4,4,1,4])
    print(res)