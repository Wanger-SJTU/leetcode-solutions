class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #if not nums:return 0
        start,end = 0,len(nums)-1
        while end >=0 and nums[end]==val:
            end -=1
        while start <= end:
            if nums[start] == val:
                nums[start],nums[end] = nums[end],nums[start]
                end -= 1
            else:
                start += 1
        return start