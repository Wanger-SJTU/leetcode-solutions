import sys

def calc(n):
    res = 0
    while n:
        res += ((n+1)//2)**2
        n//=2
    return res

n = int(sys.stdin.readline().strip())
print(calc(n))
