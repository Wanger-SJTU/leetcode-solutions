#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
import itertools
from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = list()
        n = len(nums)
        for i in range(n):
            index = bisect_left(mem, nums[i])
            if len(mem) == index:
                mem.append(nums[i])
            else:
                mem[index] = nums[i]
            print(mem)
        return len(mem)

    # TLE
    def brute(self, nums):
        if not nums: return 0
        all_list = list()
        len_nums = len(nums)
        for i in range(1, len_nums + 1):
            all_list.extend([list(per) for per in itertools.combinations(nums, i)])

        result, flag = 0, 1
        for per_list in all_list:
            for i, _ in enumerate(per_list[:-1]):
                if per_list[i] >= per_list[i + 1]:
                    flag = 0
                    continue
            if flag:
                result = max(result, len(per_list))

            flag = 1

        return result

    def DP(self, nums):
        if not nums:
            return 0

        len_nums = len(nums)
        mem = [1]*len_nums
        result = 1
        for i in range(1, len_nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    mem[i] = max(mem[i], 1 + mem[j])

            result = max(result, mem[i])

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
