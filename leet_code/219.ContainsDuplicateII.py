

from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    if len(nums) == len(set(nums)):
            return False
    dicct = {}
    for i in range(len(nums)):
        if nums[i] not in dicct:
            dicct[nums[i]] = i
        else:
            if i - dicct[nums[i]] > k:
                dicct[nums[i]] = i
            else:
                return True
    return False'
    
if __name__ == "__main__":
    containsNearbyDuplicate([1,0,1,1],1)