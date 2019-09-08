#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
# from typing import List
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.buildBST(nums)
    
    def buildBST(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left  = self.buildBST(nums[:mid])
        node.right = self.buildBST(nums[mid+1:])
        return node

# if __name__ == "__main__":
#     s = Solution()
#     s.buildBST([-10,-3, 0,5,9])
