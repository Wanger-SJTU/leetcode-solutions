
from typing import List

def missingNumber(nums: List[int]) -> int:
    nums =sorted(nums)
    for idx,item in enumerate(nums):
        if idx != item:
            return idx
    return nums[-1]+1

def CoountingSort(nums: List[int]) -> int:
    arr = [None for _ in range(len(nums)+1)]
    for item in nums:
        arr[item] = item
    for idx,item in enumerate(arr):
        if item is None:
            return idx+1

def Bit_Manipulation(nums: List[int]) -> int:
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

def Gauss_Formula(nums: List[int]) -> int:
    expected_sum = len(nums)*(len(nums)+1)//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
