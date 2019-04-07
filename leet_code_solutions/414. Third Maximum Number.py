 
def thirdMax(nums: List[int]) -> int:
    if len(set(nums)) < 3:
        return max(nums)
    else:
        return sorted(list(set(nums)))[-3]