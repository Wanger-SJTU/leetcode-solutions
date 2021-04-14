#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 不含 AAA 或 BBB 的字符串
#
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        output = ""
        a, b, i,size = 0, 0, 0, A + B

        while i < size:
            if (a < 2 and A > B) or b==2:
                output += 'a'
                b = 0
                a += 1
                A -= 1
            else:
                output += 'b'
                b += 1
                a = 0
                B -= 1
            i += 1

        return output

