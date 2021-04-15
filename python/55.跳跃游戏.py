#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0 
        for i in range(len(nums)):
            if i <= far:
                far = max(far, nums[i] + i)
            else:
                return False 
        return True




    def funcname(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,0,0]))
