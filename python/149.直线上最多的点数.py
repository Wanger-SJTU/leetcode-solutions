#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        if not points:
            return res 
        
        n = len(points)
        for i in range(n):
            pairs = {}
            duplicates = 1
            for j in range(i+1, n):
                if points[i][0]==points[j][0] and points[i][1] == points[j][1]:
                    duplicates+=1
                    continue
                dex = points[j][0]-points[i][0]
                dey = points[j][1]-points[i][1]
                d = self.gcd(dex, dey)
                if (dex//d, dey//d,) in pairs:
                    pairs[(dex//d, dey//d)]+=1
                else:
                    pairs[(dex//d, dey//d)]=1
            res = max(res, duplicates)
            for ele in pairs:
                res = max(pairs[ele]+duplicates, res)
        return res 
                
    def gcd(self, a, b):
        if b==0:
            return a
        return self.gcd(b, a%b)

if __name__ == "__main__":
    s = Solution()
    print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))