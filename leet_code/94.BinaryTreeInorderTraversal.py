# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorderIter(root, res)
        return res
        
    def inorderR(self, root, output):
        if root is None:
            return
        if root.left is not None:
            self.inorderR(root.left, output)
        output.append(root.val)
        if root.right is not None:
            self.inorderR(root.right, output)
    
    def inorderIter(self, root, output):
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop(-1)
            output.append(cur.val)
            cur = cur.right

if __name__ == "__main__":
    a = TreeNode(0)
    a.left = TreeNode(1)
    a.right = TreeNode(2)
    s = Solution()
    print(s.inorderTraversal(a))