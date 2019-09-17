

def aplusb(a,b):
    if a == 0 or b == 0:
        return a if b == 0 else b
    while b:
        a,b =a^b, (a&b)<<1 
    return a 

import random
for i in range(100000):
    x, y = random.randint(-1e9,1e9), random.randint(-1e9,1e9)
    if x+y != aplusb(x,y):
        raise ValueError