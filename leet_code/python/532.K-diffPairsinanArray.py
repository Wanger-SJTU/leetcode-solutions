class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        if k == 0:
            dic = {}
            for i in nums:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
            count = 0
            for i in dic.values():
                if i > 1:
                    count += 1
            return count

        num2 = [i+k for i in nums]
        return len(set(nums) & set(num2))