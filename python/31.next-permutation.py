#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        i,j = len(nums)-1, -1
        # find the number not in order
        while i > 0:
            if nums[i-1] < nums[i]:
                j = i-1
                break
            i -= 1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                nums[j+1:] = sorted(nums[j+1:])
                return


