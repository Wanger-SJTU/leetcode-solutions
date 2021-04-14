#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.majorityElement_Voting(nums)
    
    def majorityElement_Voting(self, nums):
        candidate, count = nums[0], 1
        for num in nums[1:]:
            if count == 0:
                candidate,count = num, 1
                continue
            count = count + 1 if candidate == num else count - 1
        return candidate

    def majorityElement_hashmap(nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # num of majorityElement > n//2
    def  majorityElement_Sorting(nums):
        return sorted(nums)[len(nums)//2]

    def Randomization(nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
if __name__ == "__main__":
    s = Solution()
    s.majorityElement_Voting([6,5,5])
