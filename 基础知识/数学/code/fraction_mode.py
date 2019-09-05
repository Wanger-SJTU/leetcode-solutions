
def qpow_mod(a, b, mod):
    r = 1
    a %= mod
    while b:
        if b & 1:
            r = (r*a) % mod
        a = int((a*a) % mod)
        b = int(b>>1)
    return r

def fraction_mod_op(a,b,mod):
    inv = qpow_mod(b,int(mod-2), mod)
    return int(a * inv)#%mod

if __name__ == "__main__":
    print(fraction_mod_op(4, 3, 1e9+7))
