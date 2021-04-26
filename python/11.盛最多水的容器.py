#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0,len(height)-1
        res = min(height[l], height[r])*(r-l)
        while l < r:
            res =max(res, min(height[l], height[r])*(r-l))
            if height[l] > height[r]:
                r -= 1
                continue
            elif height[l] < height[r]:
                l += 1
                continue
            else:
                if height[l+1] < height[r-1]:
                    r -= 1
                else:
                    l+=1
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(res)