class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for idx, char in enumerate(reversed(s)):
            res += 26**(idx)*(ord(char)-ord('A')+1)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber('BA'))