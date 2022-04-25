n = int(raw_input())
# n = int(input())
board = [[0]*n for i in range(n)]
ans = 0

# direction : up, down, left, right
# dx(dy), initial value
dx = [1, -1, 1, -1]
iv = [0, n-1, 0, n-1]
up = 0
down = 1
left = 2
right = 3

def init() :
    for i in range(n) :
        board[i] = raw_input().split()
        # board[i] = input().split()
        board[i] = [int(j) for j in board[i]]

def move(board, d) :
    nboard = [[0]*n for i in range(n)]
    if d == left or d == right :
        for i in range(n) :
            j = iv[d]
            nj = j
            while j >= 0 and j < n :
                if nboard[i][nj] == 0 :
                    if board[i][j] != 0 : nboard[i][nj] = board[i][j]
                else :
                    if nboard[i][nj] == board[i][j] :
                        nboard[i][nj] *= 2
                        nj += dx[d]
                    elif board[i][j] != 0 :
                        nj += dx[d]
                        nboard[i][nj] = board[i][j]    
                j += dx[d]

    else :
        for j in range(n) :
            i = iv[d]
            ni = i
            while i >= 0 and i < n :
                if nboard[ni][j] == 0 :
                    if board[i][j] != 0 : nboard[ni][j] = board[i][j]
                else :
                    if nboard[ni][j] == board[i][j] :
                        nboard[ni][j] *= 2
                        ni += dx[d]
                    elif board[i][j] != 0 :
                        ni += dx[d]
                        nboard[ni][j] = board[i][j]   
                i += dx[d]

    return nboard

def dfs(board, d, level) :
    global ans
    nboard = move(board, d)
    if level >= 5 : 
        for i in range(n):
            for j in range(n) :
                ans = max(ans, nboard[i][j])
        return

    for i in range(4):
        dfs(nboard, i, level+1)
    
    return 

init()
for i in range(4):
    dfs(board, i, 1)
print(ans)