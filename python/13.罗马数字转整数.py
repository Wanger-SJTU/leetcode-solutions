#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {
            "I":1,  "IV":4, "V":5,  "IX":9,
            "X":10, "XL":40,"L":50, "XC":90,
            "C":100,"CD":400,"D":500,"CM":900,"M":1000
        }
        i,j,res = 0,0,0
        while i < len(s):
            if s[i:i+2] in roman:
                res += roman[s[i:i+2]]
                i+=2
            else:
                res += roman[s[i]]
                i+=1
        return res
    
    def funcname(self, s):
        roman = {
            "I":1, "V":5,  "X":10, "L":50, 
            "C":100,"D":500,"M":1000
        }
        res = roman[s[0]]
        for i in range(1, len(s)):
            if roman[s[i-1]] < roman[s[i]]:
                res -= 2*roman[s[i-1]]
            res += roman[s[i]]
        return res
    
if __name__ == "__main__":
    s = Solution()
    a = s.funcname("IVI")
    print(a)
