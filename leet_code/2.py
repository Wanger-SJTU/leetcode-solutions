
n,m = map(int, input().split())
used = [0]*(n+1)
total = 0
for _ in range(m):
    l,r = map(int, input().split())
    for i in range(l,r+1):
        if used[i]  == 0:
            total += 1
            used[i]=1
    print(total)

