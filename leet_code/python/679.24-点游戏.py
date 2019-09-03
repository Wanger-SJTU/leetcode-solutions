#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
from operator import truediv, mul, add,sub
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums: return False
        if len(nums) == 1: return abs(nums[0] - 24) < 1e-6

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    B = [nums[k] for k in range(len(nums)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i:
                            continue
                        if op is not truediv or nums[j]:
                            B.append(op(nums[i], nums[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/24-game/solution/24dian-you-xi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

