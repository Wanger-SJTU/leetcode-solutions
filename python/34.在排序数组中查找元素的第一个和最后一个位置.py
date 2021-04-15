#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getIndex(nums, idx):
            srt,end = idx, idx
            while srt > -1 and nums[srt] == nums[idx]:
                srt -= 1
            while end < len(nums) and nums[end] == nums[idx]:
                end += 1
            return [srt+1,end-1]
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] == target:
                return getIndex(nums, mid)
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return [-1,-1]
# if __name__ == "__main__":
#     s = Solution()
#     print(s.searchRange([1], 1))
