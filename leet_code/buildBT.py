

null = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
def buildTree(nodeList):
    nodes = []
    for node in nodeList:
        nodes.append(TreeNode(node))
    for i in range(0, len(nodes)//2-1):
        if nodes[2*i+1].val is not None:
            nodes[i].left = nodes[2*i+1]
        if nodes[2*i+2].val is not None:
            nodes[i].right = nodes[2*i+2]
    idx = len(nodes)//2-1
    if nodes[idx].val is not None:
            nodes[idx].left = nodes[2*idx+1]
    if len(nodes)%2==1:
        nodes[idx].right = nodes[2*idx+2]
    return nodes[0]

if __name__ == "__main__":

    root = buildTree([5,4,8,11,null,13,4,7,2,null,null,null,1])
    print(root)