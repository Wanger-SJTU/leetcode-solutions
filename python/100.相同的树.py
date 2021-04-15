#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.isSameTreeIter(p,q)
       # return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q

    def isSameTreeRecurent(self, p: TreeNode, q: TreeNode)-> bool:
        if not p or not q:
            return True if not q and not p else False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSameTreeIter(self, p: TreeNode, q: TreeNode)-> bool:
        if not p or not q:
            return True if not q and not p else False
        stack_p, stack_q = [], []
        while p and q or stack_p and stack_q:
            while p and q:
                stack_p.append(p)
                stack_q.append(q)
                p = p.left
                q = q.left
            if p or q:
                return False
            if stack_p and stack_q:
                p,q = stack_p.pop(), stack_q.pop()
                if p.val != q.val:
                    return False
                p,q = p.right, q.right
        return True
# if __name__ == "__main__":
#     a = TreeNode(1)
#     a.right = TreeNode(2)
#     a.right.right = TreeNode(3)
#     s = Solution()
#     print(s.isSameTreeIter(a,a))
