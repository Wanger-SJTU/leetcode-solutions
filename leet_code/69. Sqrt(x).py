
# time limited
def mySqrt(x: int) -> int:
    if x < 2:
        return x
    for i in range(0, x//2+1):
        if i*i<=x and (i+1)**2 >x:
            return i

# 92ms
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        i = x//2+1
        last = 0
        while True:
            if i*i<=x and (i+1)**2 >x:
                return i
            if (i)**2 >x:
                last = i
                i = i //2
            elif  i**2 <x :
                i = (i+last)//2
## 52ms               
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        if x <= 1:
            return x
        while low <= high:
            mid =  (low + high) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid - 1            
print(mySqrt(4))