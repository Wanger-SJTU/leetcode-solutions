#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
       if not root: return 0
       return self.recursion([root], 1)

    def recursion(self, cur, depth):
        if not cur: return depth
        for node in cur:
            if not node.left and not node.right:
                return depth
        tmp = []
        for node in cur:
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        return self.recursion(tmp, depth)+1

# if __name__ == "__main__":
#     node = TreeNode(1)
#     node.right = TreeNode(2)
#     s = Solution()
#     print(s.minDepth(node))