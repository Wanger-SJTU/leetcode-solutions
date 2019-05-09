
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    i,j = 0, len(numbers)-1
    while numbers[i]+numbers[j] != target:
        if numbers[i] + numbers[j] > target:
            j-=1
        else:
            i+=1
    return i+1,j+1
