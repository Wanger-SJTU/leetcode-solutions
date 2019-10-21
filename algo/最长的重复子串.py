# 这是一个经典的动态规划问题。我们定义两个指针i和j分别指向字符串的两个位置，例如
# a b b a b a
#     i j
# 我们定义
# f(i,j) 表示S[i:i+K]和S[j:j+k] 重叠的长度，其中k表示重叠长度。如果S[i]==S[j]，那么
# f(i,j)=f(i−1,j−1)+1
# 也就是说如果i和j所指向的字母相同，那么i-1和j-1原有的重叠长度应该加上i和j的这个部分，也就是+1。

class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n, res = len(S), 0
        mem = [[0]*(n + 1) for _ in range(n+1)]
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if S[i - 1] == S[j - 1]:
                    mem[i][j] = mem[i-1][j - 1] + 1
                    res = max(res, mem[i][j])
        return res

# ————————————————
# 版权声明：本文为CSDN博主「coordinate_blog」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_17550379/article/details/89441080
