class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]
        for c in nums:
            colors[c] += 1
        idx = 0
        for i in range(3):
            for j in range(colors[i]):
                nums[idx] = i
                idx +=1
        