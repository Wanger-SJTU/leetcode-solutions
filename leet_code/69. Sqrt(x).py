

def mySqrt(x: int) -> int:
    if x < 2:
        return x
    for i in range(0, x//2+1):
        if i*i<=x and (i+1)**2 >x:
            return i

def mySqrt(x: int) -> int:
    if x < 2:
        return x
    for i in range(0, x//2+1):
        if i*i<=x and (i+1)**2 >x:
            return i
            
print(mySqrt(4))