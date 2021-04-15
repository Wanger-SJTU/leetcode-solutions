#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#
class Solution:
    def countDigitOne(self, n: int) -> int:
        return self.dp(n)
        ones, m = 0, 1
        while m <= n:
            ones += (n//m + 8) // 10 * m + (n//m % 10 == 1) * (n%m + 1)
            m *= 10
        return ones
    
    def dp(self, n):
        if n < 1: return 0
        i,delta,ans = 0,0,0
        f = [0 for _ in range(30)]
        #  f[i] => 1 ~ (10 ^ i - 1) 中 1 的出现次数
        #  f[i] = 10 * f[i - 1] + num(i - 1), num(i - 1)为 pow(10, i - 1)
        #  dealt: 已经处理完的数字（n的某个右侧部分）
        while n > 0:
            t = n % 10
            n //= 10
            f[i] = int(i*10**(i-1))
            if t == 1:
                ans += int(delta + 1 + f[i])
            elif t > 1:
                ans += t * f[i] + 10**i
            delta += t * 10**i
            i+=1
        return ans

    

if __name__ == "__main__":
    s = Solution()
    a = s.countDigitOne(12345) 
    b = s.dp(12345)
    print(a,b)