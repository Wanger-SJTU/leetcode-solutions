# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.getSubTrees(1,n)
        
        
    def getSubTrees(self, l, r):
        res = []
        if l>r:
            res.append(None)
            return res
        for i in range(l, r+1):
            left_trees = self.getSubTrees(l,i-1)
            right_trees = self.getSubTrees(i+1,r)
            for lnode in left_trees:
                for rnode in right_trees:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    res.append(root)
        return res
      

if __name__ == "__main__":
    s = Solution()
    print(s.generateTrees(3))