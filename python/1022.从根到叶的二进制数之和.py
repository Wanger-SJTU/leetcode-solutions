#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
mod = 1e9+7
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, parent_sum):
            if node:
                parent_sum = parent_sum * 2 + node.val
                if node.left or node.right:
                    return dfs(node.left, parent_sum) + dfs(node.right, parent_sum)
                else:
                    return parent_sum
            else:
                return 0
        return dfs(root, 0)

