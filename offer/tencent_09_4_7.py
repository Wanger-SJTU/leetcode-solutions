

####
def prob1():
    values = [15]
    K = 4
    rst  = 0
    for _ in range(K):
        values = list(set(values))
        if len(values) == 1 and values[0] ==1:
            break
        for value in set(values):
            if value != 1:
                rst += 1
                values.append(int(value/2))
                values.append(value - int(value/2))
                values.remove(value)
    if len(set(values)) != 1:
        rst += max(values)
    print(rst)
#####

def prob2():
    n = int(sys.stdin.readline().split()[0])
    nums = [int(each) for each in sys.stdin.readline().split()]
    carry = nums[0]
    fee = 0
    for i in range(1, len(nums)):
        fee += abs(carry)
        carry += nums[i]
    print(fee)

def prob3():
    n,k = list(map(int,(sys.stdin.readline().strip().split())))
    nums = sorted([int(each) for each in sys.stdin.readline().split()])

    tmp, max_arr = 0, max(nums)
    for _ in range(k):
        if tmp==max_arr:
            print(0)
            continue
        while True:
            min_arr = nums.pop(0)
            if min_arr != tmp:
                break
        print(min_arr - tmp)
        tmp = min_arr