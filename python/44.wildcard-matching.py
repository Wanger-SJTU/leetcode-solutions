#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def refinePattern(p):
            nums = list(p)
            if len(nums) <=1: return  "".join(nums)
            idx_i, idx_j,count = 0, 1, len(nums)

            while idx_j < len(nums):
                while nums[idx_j]==nums[idx_i] == '*' and idx_j < len(nums)-1:
                    idx_j +=1
                if not nums[idx_j]==nums[idx_i] == '*':
                    nums[idx_i+1] = nums[idx_j]
                    idx_i, idx_j = idx_i+1, idx_j+1
                else:
                    idx_j +=1
            return "".join(nums[:idx_i+1])
        #return self.isMatchRecursion(s, refinePattern(p))
        return self.isMatchIter(s,p)
        #return self.isMatchDP(s, p)
   
    def isMatchIter(self, s, p):
        i, j, iStar, jStar = 0, 0, -1, -1
        if not p:
            return False if s else True
       
        while i < len(s):   
            if  j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i, j = i+1, j+1
            elif j < len(p) and p[j]=='*':
                iStar, jStar = i, j
                j += 1
            elif iStar >= 0:
                i,iStar, j = iStar+1, iStar+1, jStar+1
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

    def isMatchDP(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]

    def isMatchRecursion(self, s, p):
        if not p:
            return True if not s and not p  else False
        if not s:
            return self.isMatchRecursion(s, p[1:]) if p[0] == "*" else False
        if p[0] == '?' or p[0] == s[0]:
            return self.isMatchRecursion(s[1:], p[1:])
        if p[0] == '*':
            return self.isMatchRecursion(s[1:], p[1:]) or \
                   self.isMatchRecursion(s[1:], p) or \
                   self.isMatchRecursion(s, p[1:])
        return False

if __name__ == "__main__":
    so =Solution()
    s = "bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab"
    p = "b*b*ab**ba*b**b***bba"
    print(so.isMatch(s, p))
    print(so.isMatchDP(s,p))
    print(so.isMatchRecursion(s,p))
