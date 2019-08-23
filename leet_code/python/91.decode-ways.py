#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
class Solution:
    def numDecodings(self, s: str) -> int:
        return self.climbStairs(s)

    def climbStairs(self, s):
        if not s or s[0] == '0': return 0
        if len(s) == 1: return len(s)
        a, b, n = 1, 1, len(s)

        for i in range(1, n):
            if s[i] == '0':
                a = 0
            if 9 < int(s[i-1:i+1]) <= 26:
                a = a+b
                b = a-b
            else:
                b = a    
        return a

    # T L E    
    def numDecodings1(self, s):
        if not s: return 0
        if s[0] == '0': return 0

        if len(s) >=2 and 0<int(s[:2]) < 27:
            if s[0] != '0':
                return self.numDecodings1(s[1:]) + self.numDecodings1(s[2:])
            else:
                return self.numDecodings1(s[2:])        
        else:
            return self.numDecodings1(s[1:])

    def numDecodings2(self, s):
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w

if __name__ == "__main__":
    s = Solution()
    res = s.climbStairs('100')
    print('res',res)
