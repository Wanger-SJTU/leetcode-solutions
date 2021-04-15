#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
        # return self.maxDepthRecursion(root)
        return self.maxDepthIter(root)

    def maxDepthRecursion(self, root, depth=0):
        if not root: return depth
        depth += 1
        return max(depth, self.maxDepthRecursion(root.left, depth),
        self.maxDepthRecursion(root.right, depth))

    def maxDepthIter(self, root):
        if not root: return 0 
        maxDepth, layerNodes = 0, [root]
        while layerNodes:
            if layerNodes[0]:
                maxDepth += 1
            tmp = []
            while layerNodes:
                node = layerNodes.pop()
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            layerNodes = tmp
        return maxDepth

