
def possibleK(n, m, nums):
    nums.sort()
    maxK = nums[-1]+m
    if sum(nums)+m <= nums[-1]*len(nums):
        minK = nums[-1]
    else:
        minK = (sum(nums)+m)%len(nums)+nums[-1]
    print(minK, maxK)

if __name__=="__main__":
    n = 2
    m =1
    nums = [3,2]
  
    possibleK(n, m, nums)