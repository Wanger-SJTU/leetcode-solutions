class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums)*len(nums)

# The greedy heuristics here is that we always 
# add |max-min| to all elements except the maximum 
# until all elements are equal.