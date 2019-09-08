#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]


if __name__ == "__main__":
    s = Solution()
    res = s.summaryRanges([0,2,3,4,6,8,9])
    print(res)

