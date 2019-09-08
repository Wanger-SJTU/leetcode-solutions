#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.count,self.n = 0,n


    def DFS(self, row, shu, pie, na):
        available = ((1 << n) - 1) & ~(shu | pie | na)  # 当前行还能放置皇后的列
        while available:                                # 枚举可用的列
            p = available & -available
            available ^= p
            if row == n - 1:
                self.count += 1
            else:
                DFS(row + 1, shu | p, (pie | p) >> 1, (na | p) << 1) # 设置标记并移位
