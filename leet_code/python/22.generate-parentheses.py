#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))

if __name__ == "__main__":
    s = Solution()
    s.generateParenthesis(3)
