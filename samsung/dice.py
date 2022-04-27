n, m, x, y, k = list(map(int, input().split()))
board = [[0]*m for i in range(n)]
dice = [0] * 7
diceMap=[1, 3, 4, 2, 5, 6]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
order = [0]*k
diceNum = 1

for i in range(n):
    board[i] = list(map(int, input().split()))
order = list(map(int, input().split()))

def rollDice(di, dice):
    s = dice[0]
    op = dice[-1]
    right = dice[1]
    left = dice[2]
    up = dice[3]
    down = dice[4]

    if di == 1 : # right
        dice[0] = right
        dice[1] = op
        dice[2]= s
        dice[5] = left
    elif di == 2 : # left
        dice[0] = left
        dice[1] = s
        dice[2] = op
        dice[5] = right
    elif di == 3 : # up
        dice[0] = up
        dice[3] = op
        dice[4] = s
        dice[5]= down
    elif di == 4 : # down
        dice[0] = down
        dice[3] = s
        dice[4] = op
        dice[5] = up

for i in range(k):
    x+= dx[order[i]]
    y+= dy[order[i]]
    if x < 0 or x >= n or y<0 or y>=m : 
        x-=dx[order[i]]
        y-=dy[order[i]]
        continue
    
    rollDice(order[i], diceMap)
    diceNum = diceMap[0]
    if board[x][y] == 0 : board[x][y] = dice[diceNum]
    else:
        dice[diceNum] = board[x][y]
        board[x][y] = 0
    print(dice[diceMap[5]])