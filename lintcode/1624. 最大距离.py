
#最大公共前缀 考虑 使用 字典树


class myTree:   #定义myTree类
    def __init__(self, val = '0', isString = False):
        self.val = val
        self.isString = isString
        self.left = self.right = None

class Solution:
    def getAns(self, s):
        root = myTree()

        for string in s:
            cur = root
            for ch in string:
                if ch == '0':
                    if cur.left is None:
                        cur.left = myTree(ch)
                    cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = myTree(ch)
                    cur = cur.right
            cur.isString = True

        self.max_len = 0
        self.get_max_len(root)
        return self.max_len


    def get_max_len(self, root):  #字典树开始搜索
        if root is None:
            return 0
        left_max_length = self.get_max_len(root.left)
        right_max_length = self.get_max_len(root.right)

        if root.left and root.right:
            self.max_len = max(self.max_len, left_max_length + right_max_length)
        if root.left and root.isString:
            self.max_len = max(self.max_len, left_max_length)
        if root.right and root.isString:
            self.max_len = max(self.max_len, right_max_length)

        return max(left_max_length, right_max_length) + 1
