
total = 0

def isValid(matrix, cur, Next):
    return matrix[Next[0]][Next[1]] > matrix[cur[0]][cur[1]]

def printMatrix(visited):
    for item in visited:
        print(item)
    print('\n')

def find(matrix, visited, cur, end, M, N):
    visited[cur[0]][cur[1]] = 1
    if cur[0] == end[0] and cur[1] == end[1]:
        global total
        total = total + 1
        printMatrix(visited)
        return
    top = cur[0]-1, cur[1]
    down = cur[0]+1, cur[1]
    left = cur[0], cur[1]-1
    right = cur[0], cur[1]+1

    if left[1] > 0 and visited[left[0]][left[1]] == 0 and isValid(matrix, cur, left):
        find(matrix,visited, left, end, M, N)
    if right[1] < M and visited[right[0]][right[1]] == 0 and isValid(matrix, cur, right):
        find(matrix, visited, right, end, M, N)
    if top[0] > 0 and visited[top[0]][top[1]] == 0 and isValid(matrix, cur, top):
        find(matrix,visited, top, end, M, N)
    if down[0] < N and visited[down[0]][down[1]] == 0 and isValid(matrix, cur, down):
        find(matrix,visited, down, end, M, N)

if __name__ == "__main__":
    N,M = 4,5
    src, end = (0,1),(3,2)
    matrix = [[0,1,0,0,0],[0,2,3,0,0],[0,0,4,5,0],[0,0,7,6,0]]
    printMatrix(matrix)
    visited = [[0 for _ in range(M)] for _ in range(N)]
    find(matrix, visited, src, end, M, N)
    print(total)

    