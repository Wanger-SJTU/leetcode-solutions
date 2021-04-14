#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_p = prices[0]
        max_profit = 0
        for item in prices[1:]:
            max_profit = max(max_profit,  item - min_p)
            min_p = min(min_p, item)
        return max_profit

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
