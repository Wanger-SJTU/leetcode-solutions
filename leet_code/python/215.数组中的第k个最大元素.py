#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthLargest2(nums, k)

    def sortAll(self, nums, k):
        return sorted(nums,reverse=True)[k]

    def findKthLargest2(self, nums, k):
        return heapq.nlargest(k, nums)[k-1]

    # O(n) time, quick selection
    def findKthLargest3(self, nums, k):
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums)+1-k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
