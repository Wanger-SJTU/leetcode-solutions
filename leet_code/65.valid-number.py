#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not len(s):return False
        haveE,haveDot,havedigit = False,False,False
        i = 0
        if s[i]=='+' or s[i]=='-':
            i+=1
        if s[i].isdigit():
            i+=1
            havedigit = True
        elif s[i]=='.':
            haveDot=True
            i+=1
        else:
            return False
        while i<len(s):
            if s[i]=='e':
                if haveE or (not havedigit):
                    return False
                else:
                    havedigit = False
                    haveE = True
                if (i+1<len(s)) and (s[i+1]=='+' or s[i+1]=='-'):
                    i+=2
                else:
                    i+=1
            elif s[i].isdigit():
                havedigit = True
                i+=1
            elif s[i] == '.':
                if haveDot or haveE:
                    return False
                else:
                    haveDot = True
                    i+=1
            else:
                return False
        return True if havedigit else False

   
    def cheat(self, s):    
        try:
            float(s.strip())
        except ValueError:
            return False
        else:
            return True
        

