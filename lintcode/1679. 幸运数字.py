class Solution:
    """
    @param n str: the number n
    @return str: the smallest lucky number  that is not less than n
    """
    def luckyNumber(self, n):
        # Write your code here.
        if len(n)&1:
            n='0'+n
        n = list(n)
        count3=0
        print(n)
        for idx, char in enumerate(n):
            if  '0'<= char <='3' and count3 < len(n)//2:
                n[idx] = '3'
                count3 +=1
            else:
                n[idx] = '5'
        return ''.join(n)
if __name__ == "__main__":
    s = Solution()
    print(s.luckyNumber("99999999"))
