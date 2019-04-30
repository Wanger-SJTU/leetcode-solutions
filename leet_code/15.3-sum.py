#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: 
            return []
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        ans = []
        nums = sorted(count)
        for i, n in enumerate(nums):
            if count[n] >= 2:
                if n == 0 and count[n] >= 3:
                    ans.append([n] * 3)
                else:
                    comp = (-2 * n)
                    if comp in count and comp != n:
                        ans.append([n] * 2 + [comp])
            if n < 0:
                twoSum = -n
                left = bisect.bisect_left(nums, twoSum - nums[-1], i + 1)
                right = bisect.bisect_right(nums, twoSum // 2, left)
                for j in nums[left:right]:
                    comp = twoSum - j
                    if comp in count and comp != j:
                        ans.append([n, j, comp])
        return ans

