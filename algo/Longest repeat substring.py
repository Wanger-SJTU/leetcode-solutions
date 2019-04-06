
# longest repeat substring

#后缀数组 
def perfix(s1, s2):
    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            count += 1
    return count

def LRS(s):
    suffix = sorted([s[::-1][:i+1][::-1] for i in range(len(s))])
    count = 0 
    for i in range(len(suffix)-1):
        count = max(count, perfix(suffix[i], suffix[i+1]))
    return count

if __name__ == "__main__":
    LRS("asaaafg")