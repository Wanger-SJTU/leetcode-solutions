#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
    
    def test(self, nums):
        colors = [0,0,0]
        for c in nums:
            colors[c] += 1
        idx = 0
        for i in range(3):
            for j in range(colors[i]):
                nums[idx] = i
                idx +=1
        print(nums)

if __name__ == "__main__":
    s = Solution()
    s.test([2,0,2,1,1,0])
        

