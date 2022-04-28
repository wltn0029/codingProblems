import copy

n, m = list(map(int, input().split()))
board = [[0]*m for i in range(n)]
# up down left right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
level3 = [(0,1), (0,2), (1,2)]
maxVal = 0

for i in range(n):
    board[i] = list(map(int, input().split()))
    maxVal = max(maxVal, max(board[i]))

visited = {}
ans = 0

def dfs(x, y, sum, level) :
    global ans 
    if level == 4 : 
        ans = max(sum, ans)
        return
    if sum + (4-level) * maxVal < ans : return 

    child = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx >= n or ny <0 or ny >=m or (nx,ny) in visited : continue
        visited[(nx,ny)] = True
        dfs(nx, ny, sum + board[nx][ny], level+1)
        del visited[(nx,ny)]
        child.append((nx, ny))
        
    if len(child) >=2 and level == 2 :
        for i1, i2 in level3 :
            if i2 == len(child) : continue
            x1, y1 = child[i1]
            x2, y2 = child[i2]
            if (x1, y1) in visited or (x2, y2) in visited: continue
            ans = max(ans, sum + board[x1][y1] + board[x2][y2])

for i in range(n) :
    for j in range(m):
        visited[(i,j)] = True
        dfs(i, j, board[i][j], 1)
        del visited[(i,j)] 

print(ans)