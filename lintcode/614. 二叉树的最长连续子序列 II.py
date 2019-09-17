
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        max_len = 0
        def helper(node):
            if not node:
                return 0,0
            nonlocal max_len
            up,down = 1,1
            left,right = helper(node.left), helper(node.right)
            if node.left:
                if node.left.val == node.val-1:
                    up = max(up, left[0]+1)
                if node.left.val == node.val+1:
                    down = max(up, left[1]+1)
            if node.right:
                if node.right.val == node.val-1:
                    up = max(up, right[0]+1)
                if node.right.val == node.val+1:
                    down = max(up, right[1]+1)
            max_len=max(max_len, up+down-1)
            return up,down
        helper(root)
        return max_len
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(0)
    s=Solution()
    print(s.longestConsecutive2(root))
