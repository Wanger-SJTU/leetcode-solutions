#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.recur(root, 0, sum)
    
    def recur(self, node, this_sum, target_sum):
        if not node: return False
        if not node.left and not node.right:
            return True if this_sum+node.val == target_sum else False
        left = self.recur(node.left, this_sum+node.val, target_sum)
        right = self.recur(node.right, this_sum+node.val, target_sum)
        return  left or right
                

# if __name__ == "__main__":
#     from buildBT import buildTree
#     null = None
#     root = buildTree([5,4,8,11,null,13,4,7,2,null,null,null,1])
#     s = Solution()
#     print(s.hasPathSum(root, 22))