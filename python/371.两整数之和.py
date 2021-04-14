#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

if __name__ == "__main__":
    s = Solution()
    print(s.getSum(1,2))
