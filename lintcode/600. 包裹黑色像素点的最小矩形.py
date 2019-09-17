from collections import deque

class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        visited,queue = set(), deque()
        queue.append((x,y))
        lefttop,rightdown = [x,y],[x,y]
        m,n = len(image), len(image[0])
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                visited.add(cur)
                lefttop[0] = min(lefttop[0], cur[0])
                lefttop[1] = min(lefttop[1], cur[1])
                rightdown[0] = max(rightdown[0], cur[0])
                rightdown[1] = max(rightdown[1], cur[1])
                if cur[0]-1 >= 0 and image[cur[0]-1][cur[1]]=="1" and (cur[0]-1, cur[1]) not in visited:
                    queue.append((cur[0]-1, cur[1]))
                if cur[1]-1 >= 0 and image[cur[0]][cur[1]-1]=="1" and (cur[0], cur[1]-1) not in visited:
                    queue.append((cur[0], cur[1]-1))
                if cur[0]+1 < m and image[cur[0]+1][cur[1]]=="1" and (cur[0]+1, cur[1]) not in visited:
                    queue.append((cur[0]+1, cur[1]))
                if cur[1]+1 < n and image[cur[0]][cur[1]+1]=="1" and (cur[0], cur[1]+1) not in visited:
                    queue.append((cur[0], cur[1]+1))
        return (rightdown[0]- lefttop[0])*(rightdown[1]-lefttop[1])

if __name__ == "__main__":
    s = Solution()
    print(s.minArea(["0010","0110","0100"], 0, 2))
