#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count,self.n = 0,n
        self.DFS(0,0,0,0)
        return self.count

    def DFS(self, row, shu, pie, na):
        available = ((1 << self.n) - 1) & ~(shu | pie | na)  # 当前行还能放置皇后的列
        while available:                                # 枚举可用的列
            p = available & -available
            available ^= p
            if row == self.n - 1:
                self.count += 1
            else:
                self.DFS(row + 1, shu | p, (pie | p) >> 1, (na | p) << 1) # 设置标记并移位


