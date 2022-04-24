a = raw_input().split()
N = int(a[0])
M = int(a[1])
board = [[] for i in range(N)]
# pos (x, y)
rx, ry, bx, by, ox, oy= [0]*6
parent = dict()
R = {}
B = {}
queue = []
visited = {}

# read input data
for i in range(N):
    board[i] = list(raw_input())
    if "R" in board[i] :
        j = board[i].index("R")
        rx, ry = (i,j)
    if "B" in board[i] : 
        j = board[i].index("B")
        bx, by = (i,j)
    if "O" in board[i] : 
        j = board[i].index("O")
        ox, oy = (i,j)

# board component : R, B, O, #, .
block = "#"
path = "."
# direction : up, down, right, left
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def calMarblePos(rx, ry, dx, dy) :
    c = 0
    while board[rx+dx][ry+dy] != block and board[rx][ry] != "O" :
        rx += dx
        ry += dy
        c += 1
    return (rx, ry, c)
    

# data form : (rx, ry, bx, by, level)
start = (rx, ry, bx, by, 0)
queue.append(start)

ans = -1
while len(queue) != 0 :
    cur = queue.pop(0)
    rx, ry, bx, by, lev = cur
    if (rx, ry, bx, by) in visited : continue
    visited[(rx, ry, bx, by)] = True

    if (rx, ry) == (ox, oy) : 
        ans = lev
        break
    elif lev >= 10 : continue
    
    for i in range(4):
        nrx, nry, rc = calMarblePos(rx, ry, dx[i], dy[i])
        nbx, nby, bc = calMarblePos(bx, by, dx[i], dy[i])
        if nbx == ox and nby == oy : continue
        if nrx == nbx and nry == nby :
            if rc > bc : 
                nrx -= dx[i]
                nry -= dy[i]
            else :
                nbx -= dx[i]
                nby -= dy[i]
        if (nrx, nry, nbx, nby) in visited : continue
        queue.append((nrx, nry, nbx, nby, lev+1))

print(ans)
    
 