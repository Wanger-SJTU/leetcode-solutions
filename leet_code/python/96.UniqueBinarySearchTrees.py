class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={}
        def help(n):
            if n in d:
                return d[n]
            if n<=2:
                d[n]=n
                return n
            result=0
            for i in range(1,n-1):
                result+=help(i)*help(n-i-1)
            result+=2*help(n-1)
            d[n]=result
            return result
        help(n)
        return d[n]

    def numTreesDP(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp =[0]*(n+1)
        dp[0]=1
        
        #each n
        for x in range(1,n+1):
            #each possible root
            for y in range(1,x+1):
                dp[x] += dp[y-1]*dp[x-y]
        return dp[n]
        
        