#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        volume = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)
            if l_max <= r_max:
                volume += l_max - height[left]
                left += 1
            else:
                volume += r_max - height[right]
                right -= 1
        return volume

    def trap_stack(self, height: List[int]) -> int:
        volume = 0
        stack,cur =[], 0
        while cur < height:
            while not stack and height[cur] > height[stack[-1]]:
                left = stack.pop(-1)
                volume += min(height[cur] - height[left])*(cur-left+1)
            stack.append(cur)
            cur += 1

        return volume
