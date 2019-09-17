"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import defaultdict
class Solution:
    """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        # write your code here
        dic = defaultdict(int)
        def helper(root):
            if not root: return 0
            if root in dic: return dic[root]
            rob = root.val
            if root.left:
                rob += helper(root.left.left)
                rob += helper(root.left.right)
            if root.right:
                rob += helper(root.right.left)
                rob += helper(root.right.right)
            noRob = helper(root.left) + helper(root.right)
            dic[root] = max(rob, noRob)
            return dic[root]
        return helper(root)
