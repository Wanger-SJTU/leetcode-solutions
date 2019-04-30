#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        for i in range(len(nums)-2):
            j,k = i+1,len(nums)-1
            while j < k:
                res_sum = nums[i]+nums[j]+nums[k]
                if res_sum == target:
                    return res_sum
                if abs(res_sum-target) < abs(result-target):
                    result = res_sum
                if res_sum < target:
                    j += 1
                else:
                    k -= 1
        return res_sum

