
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n = bin(N)
        return 2 ** (len(n) - 2) - 1 - N


if __name__ == "__main__":
    s = Solution()
    print(s.bitwiseComplement(5))
        