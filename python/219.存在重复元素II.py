#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        dicct = {}
        for i in range(len(nums)):
            if nums[i] not in dicct:
                dicct[nums[i]] = i
            else:
                if i - dicct[nums[i]] > k:
                    dicct[nums[i]] = i
                else:
                    return True
        return False

