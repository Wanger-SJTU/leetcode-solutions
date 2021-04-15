# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildBST(nums)
    
    def buildBST(self, nums):
        if not nums:
            return None
       
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left  = self.buildBST(nums[:mid])
        node.right = self.buildBST(nums[mid+1:])
        return node