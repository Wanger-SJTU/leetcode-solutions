# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        if not self.IsBalanced_Solution(pRoot.left) or not self.IsBalanced_Solution(pRoot.right):
            return False
        return abs(self.GetDepth(pRoot.left) - self.GetDepth(pRoot.right)) <= 1
    
    def GetDepth(self, pRoot):
        if pRoot is None:
            return 0 
        return max(self.GetDepth(pRoot.left), self.GetDepth(pRoot.right))+1