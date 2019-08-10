
import collections
from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    return not len(set(nums)) == len(nums)

def sortring(nums):
    nums = sorted(nums)
    for idx in range(len(nums)-1):
        if nums[idx] == nums[idx+1]:
            return True
    return False

def use_dict(nums):
    count = collections.Counter(nums)
    try:
        return max(count.values()) > 1
    except Exception as identifier:
        return True

if __name__ == "__main__":
    use_dict([1,3,4,56,2,2])
        