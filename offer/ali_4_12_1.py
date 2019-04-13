
from scipy.special import comb

def apple( m, n)
{
    if(m==0||m==1||n==1)
        return 1
    if(m<n)
        return apple(m,m)
    if(m>=n)
        return apple(m-n,n)+apple(m,n-1)
}

class Ali2(object):
    @staticmethod
    def func(M, N, K):
        global dp
        res = 0
        for i in range(1,K-1):
            a = dp[M][i]
            for j in range(1, K-i):
                b = dp[N][j]
                res += a*b
        print(res)
    
    @staticmethod
    def X_2_Y(n, m):
        global dp
        for i in range(n):
            for j in range(1, m+1):
                if j==1 or i==0:
                    dp[i][j]=1
                elif i<j:
                    dp[i][j]=dp[i][i]
                elif i>=j:
                    dp[i][j]=dp[i-j][j]+dp[i][j-1]

dp = [[0 for _ in range(100)] for _ in range(100)]
Ali2.X_2_Y(1,3)
Ali2.func(1,1,3)