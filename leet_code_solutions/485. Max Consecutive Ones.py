
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    res, tmp = 0, 0
    for item in nums:
        if item !=0:
            tmp+=1
            res = max(res, tmp)
        else:
            tmp =0
    return res