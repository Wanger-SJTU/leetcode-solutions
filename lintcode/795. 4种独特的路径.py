
class Solution:
    """
    @param m: the row
    @param n: the column
    @return: the possible unique paths
    """
    def uniquePaths(self, m, n):
        # Write your code here
        res = 0
        visited = set()
        def dfs(cur_x, cur_y):
            nonlocal res
            visited.add((cur_x, cur_y))
            if cur_x == m-1 and cur_y == n-1:
                res+=1
                visited.remove((cur_x, cur_y))
                return
            if cur_x > 0 and (cur_x-1, cur_y) not in visited:
                dfs(cur_x-1, cur_y)
            if cur_x < m-1 and (cur_x+1, cur_y) not in visited:
                dfs(cur_x+1, cur_y)
            if cur_y > 0 and (cur_x, cur_y-1) not in visited:
                dfs(cur_x, cur_y-1)
            if cur_y < n-1 and (cur_x, cur_y+1) not in visited:
                dfs(cur_x, cur_y+1)
            visited.remove((cur_x, cur_y))
        dfs(0,0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3,3))
