#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        self.addLevel(ans, 0, root)#level from 0
        return ans


    def addLevel(self, ans, level, root):
        if not root:
            return
        elif len(ans) <= level:
                ans.append([root.val])
        elif not level%2:#if it is an even level, then then level ans should be inversed, so I use extend founction
            ans[level].extend([root.val])
        else:
            ans[level].insert(0,root.val)# if it is an odd level, then level ans should be ordinal, so I use insert function
        self.addLevel(ans, level + 1, root.left)
        self.addLevel(ans, level + 1, root.right)


