a = raw_input().split()
N = int(a[0])
M = int(a[1])
board = [[] for i in range(N)]
# pos (x, y)
Rpos = (0, 0)
Bpos = (0, 0)
Opos = (0, 0)
parent = dict()
R = {}
B = {}
queue = []
visited = []

# read input data
for i in range(N):
    board[i] = list(raw_input())
    if "R" in board[i] :
        j = board[i].index("R")
        Rpos = (i,j)
    if "B" in board[i] : 
        j = board[i].index("B")
        Bpos = (i,j)
    if "O" in board[i] : 
        j = board[i].index("O")
        Opos = (i,j)

# direction : up, down, left, right
up = -1
down = 1
left = 2
right = -2
null = 0

# board component : R, B, O, #, .
block = "#"
path = "."

def calMarblePos(curPos, otherPos, di) :
    i, j = curPos
    whileCheck = True
    iUpdate = i 
    jUpdate = j
    iUpdate2 = i
    jUpdate2 = j
    if di == up :
        whileCheck = i > 0
        iUpdate = lambda x : x - 1
        jUpdate = lambda y : y
        iUpdate2 = lambda x : x + 1
        jUpdate2 = jUpdate
    elif di == down : 
        whileCheck = i < N-2
        iUpdate = lambda x : x + 1
        jUpdate = lambda y : y
        iUpdate2 = lambda x : x - 1
        jUpdate2 = jUpdate
    elif di == left : 
        whileCheck = j > 0
        iUpdate = lambda y : y
        jUpdate = lambda x : x - 1
        iUpdate2 = iUpdate
        jUpdate2 = lambda x : x + 1
    elif di == right : 
        whileCheck = j < M-2
        iUpdate = lambda y : y
        jUpdate = lambda x : x + 1
        iUpdate2 = iUpdate
        jUpdate2 = lambda x : x - 1
    else : 
        return curPos
    
    while whileCheck :
        i2 = iUpdate(i)
        j2 = jUpdate(j)
        if board[i2][j2] == block : break
        elif i2 == otherPos[0] and j2 == otherPos[1]:
            otherX, otherY = calMarblePos((i2,j2), (i, j),di)
            if otherX ==Opos[0] and otherY == Opos[1] :
                return (otherX, otherY)
            return (iUpdate2(otherX), jUpdate2(otherY))
        elif board[i2][j2] == "O":
            return (i2, j2)
        else : 
            i = i2
            j = j2
            continue
    return (i, j)

# data form : (direction, level)
start = (null, 0)
queue.append(start)
parent[start] = (null, -1)
R[start] = Rpos
B[start] = Bpos

ans = -1
while len(queue) != 0 :
    cur = queue.pop(0)
    curDir, curLev = cur
    if curLev != 0 :
        R[cur] = calMarblePos(R[parent[cur]], B[parent[cur]], curDir)
        B[cur] = calMarblePos(B[parent[cur]], R[parent[cur]], curDir)
    if (R[cur], B[cur]) in visited : continue
    visited.append((R[cur], B[cur]))
    if R[cur] == Opos and B[cur] != Opos : 
        ans = curLev
        break
    elif B[cur] == Opos or curLev >= 10 : continue
    
    for d in (up, down, right, left) :
        if curDir == -d : continue
        if calMarblePos(R[cur], B[cur], d) == R[cur] : continue
        next = (d, curLev+1)
        queue.append(next)
        parent[next] = cur

print(ans)
    
 