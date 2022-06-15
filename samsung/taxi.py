from collections import deque

n, m, gas = list(map(int, input().split()))
board = [[0]*n for i in range(n)]
block = -555
x, y = 0, 0
dest = {}
# up down left right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# for impossible situation
impossible = 555

for i in range(n):
    board[i] = list(map(int, input().split()))
    for j in range(n):
        if board[i][j] == 1 : board[i][j] = block

x, y = list(map(int, input().split()))
x-=1
y-=1

for i in range(1, m+1):
    sx, sy, tx, ty = list(map(int, input().split()))
    board[sx-1][sy-1] = i
    dest[(sx-1, sy-1)] = (tx-1, ty-1)
# print(board)

def bfs(x, y, t = None) :
    queue = deque()
    visited = {}    
    target = (21, 21) if t is None else t
    ans = impossible

    queue.append((x,y,0))

    while queue :
        x, y, level = queue.popleft()
        if (x,y) in visited : continue
        if level > ans or gas - level < 0: break
        visited[(x,y)] = True
        if t is None and board[x][y] > 0 :
            ans = min(ans, level)
            target = min(target, (x,y))
            continue
        elif t is not None and t[0] == x and t[1] == y :
            ans = level
            break
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or nx >= n or ny < 0 or ny >= n or \
                (nx,ny) in visited or board[nx][ny] == block : continue
            queue.append((nx, ny, level+1))

    return (target[0], target[1], ans)

def takePassenger(x,y):
    global gas
    sx, sy, sd = bfs(x,y)
    gas -= sd
    if gas <0 or sd == impossible : return None
    board[sx][sy] = 0
    # print("TAKE PASSENGER start ", sx, sy, sd)

    tx, ty = dest[(sx, sy)]
    tx, ty, td = bfs(sx, sy, (tx, ty))
    # print("TAKE PASSENGER end", tx, ty, td)
    gas -= td
    if gas < 0 or sd == impossible : return None
    del dest[(sx,sy)]

    gas += td*2
    # print("TAKE PASSENGER gas", gas)
    return tx, ty

for i in range(m):
    res = takePassenger(x, y)
    if res is None :
        gas = -1
        break
    x, y = res

print(gas)