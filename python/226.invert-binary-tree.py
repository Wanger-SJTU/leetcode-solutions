#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.iter(root)

    def recur(self,root):
        if root:
            root.left, root.right = self.recur(root.right), self.recur(root.left)
            return root
    
    def iter(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right,node.left
                stack += [node.left, node.right]
        return root

