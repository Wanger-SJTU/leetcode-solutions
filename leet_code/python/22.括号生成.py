#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, res=[]):
            if left:
                generate(p+'(', left-1, right)
            if right > left:
                generate(p+')', left, right-1)
            if not right:
                res += [p]
            return res
        return generate('', n, n)


