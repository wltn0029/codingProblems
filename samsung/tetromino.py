import copy

n, m = list(map(int, input().split()))
board = [[0]*m for i in range(n)]
# up down left right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = {}
ans = 0
maxVal = 0

for i in range(n):
    board[i] = list(map(int, input().split()))
    maxVal = max(maxVal, max(board[i]))

def dfs(x, y, sum, level) :
    global ans 
    if level == 4 : 
        ans = max(sum, ans)
        return
    if sum + (4-level) * maxVal < ans : return 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx >= n or ny <0 or ny >=m or (nx,ny) in visited : continue
        if level == 2 :
            visited[(nx,ny)] = True
            dfs(x, y, sum + board[nx][ny], level+1)
            del visited[(nx,ny)]

        visited[(nx,ny)] = True
        dfs(nx, ny, sum + board[nx][ny], level+1)
        del visited[(nx,ny)]


for i in range(n) :
    for j in range(m):
        visited[(i,j)] = True
        dfs(i, j, board[i][j], 1)
        del visited[(i,j)] 

print(ans)