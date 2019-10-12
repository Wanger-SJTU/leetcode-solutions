#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
    def mathop(self, x):
        if x < 0: return False
        hi = 1
        while x // hi > 10:
            hi *= 10
        while hi > 10:
            a,x = divmod(x, hi)
            x,b = divmod(x, 10)
            hi = hi // 100
            if a != b:
                return False
        return True
if __name__ == "__main__":
    s = Solution()
    print(s.mathop(13221))
