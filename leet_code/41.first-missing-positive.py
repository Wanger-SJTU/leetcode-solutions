#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:return 1
        for i in range(len(nums)):
            while 0<=nums[i]-1<len(nums) and nums[nums[i]-1]!= nums[i]:
                tmp = nums[i]-1 
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

# if __name__ == "__main__":
#     s = Solution()
#     a = s.firstMissingPositive([3,4,-1,1])
#     print(a)