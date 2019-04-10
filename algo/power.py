
def pow(base,exp):
    res = 1
    while exp != 0:
        if exp & 1:
            res = res * base        
        base = base *base
        exp >>= 1
    return res

def pow_new(base, exp):
    res = 1
    count= -1*exp  if exp<0 else exp 
    base = 1 /base if exp<0 else base
    while count>0:
        if count & 1:
            res = res * base
            count -=1
        else:
            res = res * res
            count = count //2
    return res

if __name__ == "__main__":
    print(pow_new(2,3))