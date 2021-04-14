#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
class ExpNode:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class Solution:
    def calculate(self, s: str) -> int:
        if not s: return "0"
        operator = {"+","-","*","/"}
        stack,num,sign = [],0,"+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
        return sum(stack)

