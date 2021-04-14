
from functools import lru_cache


@lru_cache(maxsize=None)
def fib4(n: int) -> int:  # same definition as fib2()
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursive case


def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

def matrix_pow(M, N):
    res = [[0 for _ in range(2)] for _ in range(2)]    
    for i in range(2):
        for j in range(2):
            tmp=0
            for k in range(2):
                tmp += M[i][k]*N[k][j]
            res[i][j] = tmp
    return res


def fib7(n: int) -> int:
    if n == 0: return n  # special case
    fib0: int = 0  # initially set to fib(0)
    fib1: int = 1  # initially set to fib(1)
    base = [[1,1],[1,0]]
    res  = [[1,0],[0,1]]
    while n > 0:
        # print(res)
        if n % 2 ==1:
            res = matrix_pow(res,base)
        base = matrix_pow(base,base)
        n = n//2
    fib_n = res[1][0]
    return fib_n