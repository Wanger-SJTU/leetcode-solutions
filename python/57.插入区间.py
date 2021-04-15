#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l,r = newInterval[0],newInterval[1]
        left,right=[],[]
        for item in intervals:
            if item[1] < l:
                left.append(item)
            elif item[0] > r:
                right.append(item)
            else:
                l = min(l, item[0])
                r = max(r, item[1])
        return left+[[l,r]]+right

if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1,3],[6,9]],[2,5]))
