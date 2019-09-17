def strStr(source, target):
    # Write your code here
    if not source or not target:
        return 0 if not target else -1

    for i in range(len(source)-len(target)+1):
        if set((source[i:i+len(target)],)) == set((target,)):
            print(set(target))
            return i
    return -1

if __name__ == "__main__":
    print(strStr("tartarget", "target"))