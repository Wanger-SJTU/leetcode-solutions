#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.bitMethod2(nums)
    
    def hashMethod(self, nums):
        from collections import Counter
        c = Counter(nums)
        for k,v in c.items():
            if v == 1:
                return k

    def bitMethod(self, nums):
        ans = 0
        for i in range(32):
            cnt = 0
            bit = 1 << i
            for j in nums:
                if j & bit:
                    cnt += 1
            if cnt % 3 != 0:
                ans |= bit
        return ans

    #利用二进制模拟a进制的方法。a为3.
    def bitMethod2(self, nums):
        one, two = 0, 0
        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            one, two = one & ~three, two & ~three
        return one

