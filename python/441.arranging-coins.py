#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
class Solution:
    def arrangeCoins(self, n: int) -> int:
        import math
        return math.floor(math.sqrt(2*n+1/4)-1/2)

# if __name__ == "__main__":
#     s =Solution()
#     print(s.arrangeCoins(8))
