
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# preOrder
def PreOrderTravelRecursion(root : TreeNode, res:list):
    if not root: return
    res.append(root.val)
    InOrderTravelRecursion(root.left,  res)
    InOrderTravelRecursion(root.right, res)

def PreOrderTravelIter(root:TreeNode):
    res, stack = [],[]
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    return res

# inOrder

def InOrderTravelRecursion(root : TreeNode, res:list):
    if not root: return
    InOrderTravelRecursion(root.left, res)
    res.append(root.val)
    InOrderTravelRecursion(root.right, res)

def InOrderTravelIter(root:TreeNode):
    res, stack = [],[]
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop(-1)
            res.append(root.val)
            root = root.right
    return res

# postOrder
def PostOrderTravelRecursion(root : TreeNode, res:list):
    if not root: return
    InOrderTravelRecursion(root.left, res)
    InOrderTravelRecursion(root.right, res)
    res.append(root.val)

def PostOrderTravelIter(root:TreeNode):
    p,pre = root, None
    res, stack = [],[p]
    while stack:
        p = stack[-1]
        if (not p.left and not p.right) or\
            (not pre and pre == p.left) or pre == p.right:
            res.append(p.val)
            stack.pop(-1)
            pre = p
        else:
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.right)
    return res