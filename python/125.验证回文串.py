#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r =0,len(s)-1
        
        while l<=r:
            if not s[l].isalpha() and not s[l].isdigit():
                l+=1
                continue
            if not s[r].isalpha() and not s[r].isdigit():
                r-=1
                continue
            if s[l].lower() == s[r].lower():
                l,r=l+1,r-1
                continue
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    res =s.isPalindrome("A man, a plan, a canal: Panama")
    print(res)


