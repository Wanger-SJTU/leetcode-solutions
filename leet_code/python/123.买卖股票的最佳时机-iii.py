#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        len_prices = len(prices)
        buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0

        for i in range(1, len_prices):
            buy1  = max(buy1,  -prices[i])#尽可能低的买入
            sell1 = max(sell1, buy1 + prices[i])#尽可能大的利润
            buy2  = max(buy2,  sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return sell2


