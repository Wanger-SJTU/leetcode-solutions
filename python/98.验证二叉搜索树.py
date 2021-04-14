#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        if not self.BSTLeft(root.left, root.val) or not self.BSTRight(root.right, root.val):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def BSTLeft(self, root, value):
        if not root:
            return True
        if root.val >= value:
            return False
        return self.BSTLeft(root.left, value) and self.BSTLeft(root.right, value)

    def BSTRight(self, root, value):
        if not root:
            return True
        if root.val <= value:
            return False
        return self.BSTRight(root.left, value) and self.BSTRight(root.right, value)
