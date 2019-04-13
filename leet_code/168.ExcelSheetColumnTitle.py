#36ms

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        digit2char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        resList = []
        
        while(n):
            n -= 1
            resList.append(n % 26)
            n = n//26
        res = ""
        reslength = len(resList)
        for i in range(reslength):
           res = digit2char[resList[i]] + res
        return res