class Solution:
    """
    @param maze: the map
    @return: output the minimal number of steps you will take
    """
    def minSteps(self, maze):
        # Write your code here
        srt,end = None,None
        objs, visited,res = set(),set(), float('inf')
        for i, row in enumerate(maze):
            for j, pos in enumerate(row):
                if pos.lower() == 's':
                    srt = (i,j)
                if pos.lower() == 't':
                    end = (i,j)
                if pos.isdigit():
                    objs.add(pos)
        print(objs,srt,end)
        def dfs(x,y, path):
            nonlocal res
            if x == end[0] and y == end[1]:
                if not objs:
                    res = min(res, path)
                return
            if x > 0 and maze[x-1][y] != "*":
                if maze[x-1][y].isdigit():
                    if maze[x-1][y] in objs:
                        objs.remove(maze[x-1][y])
                        dfs(x-1, y, path+1)
                        objs.add(maze[x-1][y])
                else:
                    dfs(x-1, y, path+1)

            if x < len(maze)-1  and maze[x+1][y] != "*":
                if maze[x+1][y].isdigit():
                    if maze[x+1][y] in objs:
                        objs.remove(maze[x+1][y])
                        dfs(x+1, y, path+1)
                        objs.add(maze[x+1][y])
                else:
                    dfs(x+1, y, path+1)
            if y > 0  and maze[x][y-1] != "*":
                if maze[x][y-1].isdigit():
                    if maze[x][y-1] in objs:
                        objs.remove(maze[x][y-1])
                        dfs(x, y-1, path+1)
                        objs.add(maze[x][y-1])
                else:
                    dfs(x, y-1, path+1)

            if y < len(maze[0])-1 and maze[x][y+1] != "*":
                if maze[x][y+1].isdigit():
                    if maze[x][y+1] in objs:
                        objs.remove(maze[x][y+1])
                        dfs(x, y+1, path+1)
                        objs.add(maze[x][y+1])
                else:
                    dfs(x, y+1, path+1)



        dfs(srt[0],srt[1],1)
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.minSteps(["T1S.",
                      ".*0*",
                      "....",
                      "..*."]))
