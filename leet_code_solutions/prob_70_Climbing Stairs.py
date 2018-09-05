
# for given n steps stairs 
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

def brute_force(n):
  if n == 1 or n == 2:
    return n
  return brute_force(n-1)+brute_force(n-2)

memo = {}
def recursion_memo(n, memo):

    if n==1 or n ==2:
        return n
    if n in memo.keys():
        return memo[n]
    value = recursion_memo(n-1, memo) + recursion_memo(n-2, memo)
    memo.update({n:value})
    return memo[n]

def dynamic(n):
    if n == 1 or n == 2:
        return n
    result = [0]*(n)
    result[0] =1
    result[1] =2
    for i in range(2, n):
        result[i] = result[i-1]+result[i-2]
    return result[n-1]

if __name__ == '__main__':
  print(recursion_memo(10, memo))