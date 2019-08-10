
def searchInsert(nums: List[int], target: int) -> int:
    for idx in range(len(nums)):
        if nums[idx]>=target:
            return idx
    return len(nums)