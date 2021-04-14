#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted((nums1, nums2), key=len)
        # a 短数组 b 长数组
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) // 2
            # b[0:after-i] 长数组 left
            if after-i-1 < 0 or a[i] >= b[after-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])##??
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0

    def get_median(self, nums1, nums2):
        nums = []
        idx1 = 0
        idx2 = 0
        while idx1 <len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2]:
                nums.append(nums1[idx1])
                idx1 += 1
            else:
                nums.append(nums2[idx2])
                idx2 += 1
        while idx1 < len(nums1):
            nums.append(nums1[idx1])
            idx1 += 1
        while idx2 < len(nums2):
            nums.append(nums2[idx2])
            idx2 += 1
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2]+nums[len(nums)//2-1])/2
        else:
            return nums[len(nums)//2+1]


    def mergeSort(self, nums1, nums2):
        total = len(nums1) + len(nums2)
        idx1,idx2 = 0,0
        i,left,right = 0,-1,-1
        while i <= total//2:
            left = right
            if idx1 < len(nums1) and (idx2 >= len(nums2) or nums1[idx1] < nums2[idx2]):
                right = nums1[idx1]
                idx1+=1
            else:
                right = nums2[idx2]
                idx2+=1
            i += 1
        return (left+right)/2.0 if total& 1 ==0 else right


if __name__ == "__main__":
    s = Solution()
    a = s.mergeSort([1,3],[2])
    print(a)