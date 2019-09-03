

from typing import List

#brute force
class Solution1:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            previous = nums[-1] #initiate a first previous
            for i in range(len(nums)):
                temp = nums[i] #hodl nums[i]
                nums[i] = previous #overwrite the current index
                previous = temp #swap the value
        logging.debug(f"nums: {nums}")

# Using Extra Array
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    a = [0] * len(nums)
    for i in range(len(nums)):
        a[(i+k)%len(nums)] = nums[i] #recycle

    for i in range(len(nums)):
        nums[i] = a[i]

# one-pass
def rotate(nums, k):
    k = k % len(nums)
    count, start = 0, 0
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
# 3n
def rotateArray(nums, k):
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    k=k%len(nums)
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
if __name__ == "__main__":
    rotate([1,2,3,4,5],2)
