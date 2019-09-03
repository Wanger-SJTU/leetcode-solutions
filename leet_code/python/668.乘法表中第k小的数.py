#
# @lc app=leetcode.cn id=668 lang=python3
#
# [668] 乘法表中第k小的数
#

def calc(item):
    return item[0]*item[1]

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 0, m * n
        while lo < hi: #O(mlog(mn))
            mid = (lo + hi) // 2
            if self.helper(m, n, k, mid):
                lo = mid + 1
            else:
                hi = mid
        return lo

    def helper(self, m, n, k, possible): # O(m)
        res = 0
        for i in range(1, m+1):
            res += min(n, possible//i)
        return res < k

if __name__ == "__main__":
    s = Solution()
    print(s.findKthNumber(3,3,5))
