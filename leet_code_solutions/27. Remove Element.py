
from typing import List

def removeElement_0(nums: List[int], val: int) -> int:       
    while True:
        try:
            nums.remove(val)
        except ValueError:
            break
    return len(nums)

def removeElement_1(nums: List[int], val: int) -> int:       
    idx_i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[idx_i] = nums[j]
            idx_i+=1
    return idx_i

def removeElement_2(nums: List[int], val: int) -> int:       
    idx_i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[idx_i] = nums[j]
            idx_i+=1
    return idx_i

if __name__ == "__main__":
    removeElement([0,1,2,2,3,0,4,2], 2)