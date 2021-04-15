#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res  = []
        candidates.sort()
        def dfs(nums, target, path):
            if target < 0: return 
            if target == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]: continue
                if nums[i] > target: break
                dfs(nums[i+1:], target-nums[i], path+[nums[i]])
        dfs(candidates, target, [])
        
        return res

# if __name__ == "__main__":
#     s = Solution()
#     print(s.combinationSum2([10,1,2,7,6,1,5], 8))
