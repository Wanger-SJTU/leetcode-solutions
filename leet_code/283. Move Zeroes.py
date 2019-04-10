
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    last =0
    for idx,item in enumerate(nums):
        if item !=0:
            nums[last], nums[idx] = nums[idx],nums[last]
            last +=1