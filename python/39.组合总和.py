#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
import bisect
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.biSearch(candidates, target, [], res)
        return res

    def search(self, candidates, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for idx,item in enumerate(candidates):
            self.search(candidates[idx:], target-item, path+[item], res)

    def biSearch(self, candidates, target, path, res):
        if not candidates or target < 0:
            return
        if target == 0:
            res.append(path)
            return
        id_s = bisect.bisect_left(candidates, target)

        for idx,item in enumerate(candidates[:id_s+1]):
            self.biSearch(candidates[idx:id_s+1], target-item, path+[item], res)

if __name__ == "__main__":
    s = Solution()
    res = s.combinationSum([2,3,5], 8)
    print(res)
