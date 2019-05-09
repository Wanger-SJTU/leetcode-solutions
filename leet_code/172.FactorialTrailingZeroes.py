

class Solution:
    def trailingZeroes_brute(self, n: int) -> int:
        count =0
        for i in range(1, n+1):
            while i % 5==0 and i > 0:
                count+=1
                i = i//5
        return count
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        while (n):
            ret += n//5
            n /= 5
        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes_brute(1808548329))