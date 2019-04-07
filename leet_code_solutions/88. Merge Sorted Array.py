
from typing import List
'''
The number of elements initialized in 
    nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space 
(size that is greater or equal to m + n) 
to hold additional elements from nums2.
'''
 def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if not n: 
        return
    i, j = m - 1, n - 1
    index = m + n - 1
    while j >= 0:
        if i < 0 or nums1[i] <= nums2[j]:
            nums1[index] = nums2[j]
            j -= 1
        else:
            nums1[index] = nums1[i]
            i -= 1
        index -= 1

if __name__ == "__main__":
    merge([1,2,3,0,0,0],[2,5,6])