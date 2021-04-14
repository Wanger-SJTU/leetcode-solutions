#
# @lc app=leetcode.cn id=587 lang=python3
#
# [587] 安装栅栏
# 这是一道求凸包的题目，
# 是计算几何中的经典问题。凸包问题有好几种解法，
# 下面的代码只是给出了其中一种。
# 更详细的说明，
# 读者可以参照：凸包问题的五种解法。
# http://blog.csdn.net/bone_ace/article/details/46239187


from functools import cmp_to_key
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        N = len(points)
        if N <= 3: return points
        lb = min(points, key = lambda p: (p[1], p[0]))
        ccw = lambda p1, p2, p3: (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        dsquare = lambda p1, p2: (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        cmp = lambda p, q: ccw(lb, q, p) or dsquare(p, lb) - dsquare(q, lb)
        points.sort(key=cmp_to_key(cmp))
        x = N - 1
        while x and ccw(lb, points[x], points[x - 1]) == 0: x -= 1
        points = points[:x] + points[x:][::-1]
        stack = [points[0], points[1]]
        for x in range(2, N):
            while len(stack) > 1 and ccw(stack[-2], stack[-1], points[x]) < 0: stack.pop()
            stack.append(points[x])
        return stack

