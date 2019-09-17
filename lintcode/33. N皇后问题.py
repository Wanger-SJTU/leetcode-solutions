
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        res = []
        def check(pre,cur):
            for col in pre:
                if col & curRow:
                    return False
            ## panduan
            return False  if (cur << 1) & col or (cur >> 1) & col else True

        def dfs(i, path):
            print(i)
            if i == n:
                res.append(path)
                return
            curCol = 1
            for idx in range(n):
                if check(path, curCol<<idx):
                    dfs(i+1, path+[curCol<<idx])
        curRow = 1
        for i in range(n):
            dfs(1, [curRow<<i])
        print(len(res))

if __name__ == "__main__":
    s=Solution()
    s.solveNQueens(8)
