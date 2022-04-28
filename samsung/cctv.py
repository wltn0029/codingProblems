import copy
n, m = list(map(int, input().split()))
board = [[0]*m for i in range(n)]
cctv = []
cctvPos = []
dir = [[], [[0], [1], [2], [3]], [(0, 1), (2,3)], [(2, 0), (2, 1), (3, 0), (3, 1)],\
       [(0, 1,2), (0,1,3), (1,2,3),(0,2,3)], [(0, 1, 2, 3)]]
# right left up down
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
ans = m*n

for i in range(n):
    board[i] = list(map(int, input().split()))
    for j in range(m):
        if board[i][j] != 6 and board[i][j] != 0 :
            cctv.append(board[i][j])
            cctvPos.append((i,j))

def watch(cx, cy, cd, nb):
    while cx>=0 and cx<n and cy>=0 and cy<m :
        if nb[cx][cy] == 0 : nb[cx][cy] = "#"
        elif nb[cx][cy] == 6 : break
        cx+=dx[cd]
        cy+=dy[cd]
    
def sumBlindSpot(arr):
    nboard = copy.deepcopy(board)
    for i, d in enumerate(arr):
        cx, cy = cctvPos[i]
        for i in d:
            watch(cx, cy, i, nboard)
        
    sum = 0
    for i in range(n):
        for j in range(m):
            if nboard[i][j] == 0 : sum+=1
    return sum

def dfs(arr, level):
    global ans
    if level == len(cctv)-1 : 
        ans = min(ans, sumBlindSpot(arr))
        return 
    nlevel = level +1
    # print(nlevel)
    for i in range(len(dir[cctv[nlevel]])) :
        dfs(arr+[dir[cctv[nlevel]][i]], nlevel)

if len(cctv) == 0 : print(sumBlindSpot([]))
else :
    for i in range(len(dir[cctv[0]])) :
        dfs([dir[cctv[0]][i]], 0)
    print(ans)
