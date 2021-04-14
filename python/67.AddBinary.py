
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        leng = max(len(a), len(b))
        a = a[::-1]
        b = b[::-1]
        res = ''
        sign = 0
        for i in range(leng):
            adigit = int(a[i]) if i < len(a) else 0  
            bdigit = int(b[i]) if i < len(b) else 0  
            sign, digit= divmod(adigit+bdigit+sign, 2)
            res += str(digit)
        if sign == 1:
            res += str(sign)
        return res[::-1]