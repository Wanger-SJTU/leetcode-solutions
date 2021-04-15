class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack:
            return -1 if needle else 0
        if not needle: return 0
        i,j,c = 0,0,0
        for i in range(len(haystack)-len(needle)+1):
            c = 0
            for j in range(len(needle)):
                if haystack[i] == needle[j]:
                    c = c + 1
                    j = j + 1
                    i = i + 1
                else:
                    break
            i = i - c
            if c == len(needle):
                return i 
        return -1