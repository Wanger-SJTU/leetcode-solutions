#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
# from typing import List

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        stack = [root]
        while stack:
            tmp = []
            for node in stack:
                tmp.append(node.val)
            res.append(tmp)
            tmp = []
            for node in stack:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            stack = tmp
        return list(reversed(res))
# if __name__ == "__main__":
#     a = TreeNode(3)
#     a.left = TreeNode(9)
#     a.right = TreeNode(20)
#     a.right.left = TreeNode(15)
#     a.right.right = TreeNode(7)
#     s = Solution()
#     print(s.levelOrderBottom(a))