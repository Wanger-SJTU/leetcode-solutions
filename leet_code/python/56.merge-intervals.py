#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:return []
        intervals = sorted(intervals, key=lambda x:x[0])
        new_res = []
        left,right = intervals[0][0], intervals[0][1]
        for item in intervals[1:]:
            if left <= item[0] <= right:
                right = max(right, item[1])
            else:
                new_res.append([left,right])
                left,right = item[0],item[1]
        new_res.append([left,right])
        return new_res

if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))