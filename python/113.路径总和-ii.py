#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res  = []
        if not root: return res
        def dfs(root, sum, path):
            if not root.left and not root.right:
                if sum == root.val:
                    res.append(path+[root.val])
                return
            if root.left:
                dfs(root.left,  sum-root.val, path+[root.val])
            if root.right:
                dfs(root.right, sum-root.val, path+[root.val])
        dfs(root, sum, [])
        return res

