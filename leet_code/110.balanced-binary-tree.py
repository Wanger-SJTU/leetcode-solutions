#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.iteration(root)
    

    def iteration(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True

    def getDepth(self, root):
        if not root: return 0
        return max(self.getDepth(root.left),
            self.getDepth(root.right))+1
        
    def recursion(self, root):
        if not root: return True
        res = self.recursion(root.left) and self.recursion(root.right)
        res = res and \
            abs(self.getDepth(root.left) - self.getDepth(root.right)) < 2
        return res

