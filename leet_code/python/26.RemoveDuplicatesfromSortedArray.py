from typing import List
def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <=1:
        return  len(nums)
    idx_i, idx_j = 0, 1
    count = len(nums)

    while idx_j < len(nums):
        while nums[idx_j]==nums[idx_i] and idx_j < len(nums)-1:
            idx_j +=1
        if nums[idx_j] != nums[idx_i]:
            nums[idx_i+1] = nums[idx_j]
            idx_i, idx_j = idx_i+1, idx_j+1
        else:
            idx_j +=1
    return idx_i+1

if __name__ == "__main__":
    print(removeDuplicates([0,0]))
