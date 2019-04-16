import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 0
        high = int(math.sqrt(num))
        for i in range(high, 0,-1):
            if num%i==0:
                res+=i
                res+= num//i if i != 1 else 0
        res = res - high if high*high == num else res
        return num == res 

if __name__ == "__main__":
    a =Solution()
    print(a.checkPerfectNumber(28))