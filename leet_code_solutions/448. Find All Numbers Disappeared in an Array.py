
from typing import List

#160 ms
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    if not nums:
        return []
    counter = [None for _ in range(len(nums))]
    res = []
    for item in nums:
        counter[item-1] = item-1
    for idx, item in enumerate(counter):
        if item is None:
            res.append(idx+1)
    return res

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    l = len(nums)
    nums = set(nums)
    return [i for i in range(1, l+1) if i not in nums]