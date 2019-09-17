

def calc(n):str
    if n <= 0:return []
    if n == 1:return list(range(10))
    store = list(map(lambda x: pow(x,n),range(10)))
    for num in range(10**(n-1), 10**n):
        res = sum(map(lambda x: store[x], map(int, str(num))))    
        if res==num:
            print(num)

if __name__ == "__main__":
    calc(8)