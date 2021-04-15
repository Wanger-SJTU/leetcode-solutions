#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        s = self.countAndSay(n-1)+"*"
        count, res = 1, ""
        for idx, char in enumerate(s[:-1]):
            if char == s[idx+1]:
                count += 1
            else:
                res = res + str(count)+s[idx]
                count = 1
        return res

# if __name__ == "__main__":
#     s = Solution()
#     print(s.countAndSay(3))

