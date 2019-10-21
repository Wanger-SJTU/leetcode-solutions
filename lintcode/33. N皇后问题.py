class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        res, q = [], [-1] * n   # cnt 用计数，q用于已经放的位置，例如q[2]=3 表示第3行的放到了第4个位置

        def dfs(k, n):
            if k == n:
                tmp = []
                for i in range(n):  # 输出一个结果
                    s = ''
                    for j in range(n):
                        s += 'Q' if q[i] == j else '.'
                    tmp.append(s)
                res.append(tmp)
            else:
                for j in range(n):  # 一行一行的进行深度搜索
                    if self.place(k, j, q):
                        q[k] = j
                        dfs(k+1, n)
        dfs(0, n)
        return res

    def place(self, k, j, q):  # 判断该位置是否可以放一个棋子
        for i in range(k):
            if q[i] == j or abs(q[i]-j) == abs(i-k):  # 不同列，不同斜线
                return 0
        return 1
