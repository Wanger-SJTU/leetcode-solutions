

from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    a = [0] * len(nums)
    for i in range(len(nums)):
        a[(i+k)%len(nums)] = nums[i] #recycle

    for i in range(len(nums)):
        nums[i] = a[i]

def rotate(nums, k):
    k = k % len(nums)
    count = 0
    start = 0
    while count < len(nums):
        current = start 
        prev = nums[start] #store the value in the position
        
        while True:
            next = (current + k) % len(nums) #
            temp = nums[next] #store it temporaly 
            nums[next] = prev #overide the next 
            prev = temp #reset prev
            current = next #reset current
            count += 1

            if start == current:
                break 
        
        start += 1
if __name__ == "__main__":
    rotate([1,2,3,4,5],2)