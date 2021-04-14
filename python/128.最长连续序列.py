#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        maxLen=0
        while num:
            n=num.pop()
            i,l1,l2=n+1,0,0
            while i in num:
                num.remove(i)
                i,l1=i+1,l1+1
            i=n-1
            while i in num:
                num.remove(i)
                i,l2=i-1,l2+1
            maxLen=max(maxLen,l1+l2+1)
        return maxLen

