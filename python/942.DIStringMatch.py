

def diStringMatch(S: str):
    lo, hi = 0, len(S)
    res = []
    for c in S:
        if c == 'I':
            res.append(lo)
            lo+=1
        else:
            res.append(hi)
            hi-=1
    return res+[lo]

print(diStringMatch("IDIDID"))