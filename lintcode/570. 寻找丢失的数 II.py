class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here

        total = [0]*n

        def dfs(str):
            res = -1
            if not str:
                return total.index(0)+1
            if str[0] == '0':
                return res
            if int(str[0]) <= n and total[int(str[0])-1] == 0:
                total[int(str[0])-1]=1
                res = dfs(str[1:])
                if res != -1: return res
                total[int(str[0])-1]=0
            if int(str[:2]) <= n and total[int(str[:2])-1]==0:
                total[int(str[:2])-1]=1
                res = dfs(str[2:])
                if res != -1: return res
                total[int(str[:2])-1]=0
            return res
        return dfs(str)

if __name__ == "__main__":
    import random
    N = random.randint(1,30)
    miss = random.randint(1, N)
    str = ''.join(list(map(str,range(1,miss)))+
                    list(map(str,range(miss+1,N+1))))
    s = Solution()
    if (miss != s.findMissing2(N, str)):
        print(str, miss)
