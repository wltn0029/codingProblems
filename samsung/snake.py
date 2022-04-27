# global variable
n = int(raw_input())
board = [[0]*n for i in range(n)]
conversionTime = {}
conversionPlace = {}
apple = "a"
snake = "s"
# direction : right down left up
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def init() :
    k = int(raw_input())
    for i in range(k):
        x, y = [int(j) for j in raw_input().split()]
        board[x-1][y-1] = apple
    l = int(raw_input())
    for i in range(l):
        c = raw_input().split()
        conversionTime[int(c[0])] = c[1]
    board[0][0] = snake

def convertDirection(d, convert) :
    dangle = 1 if convert == "D" else 3
    return (d+dangle)%4

def doGame() :
    time = 0
    hx, hy = 0, 0
    tx, ty = 0, 0
    hd = 0
    td = 0

    while True :
        time += 1
        hx += dx[hd]
        hy += dy[hd]
        if not(hx >= 0 and hx < n) or not(hy >= 0 and hy < n) or board[hx][hy] == snake:
            return time

        bv = board[hx][hy]
        board[hx][hy] = snake
        if bv != apple :
            board[tx][ty] = 0
            if (tx, ty) in conversionPlace :
                td = conversionPlace[(tx, ty)]
                del conversionPlace[(tx, ty)]
            tx += dx[td]
            ty += dy[td]
        
        if time in conversionTime:
            nd = convertDirection(hd, conversionTime[time])
            hd = nd
            conversionPlace[(hx, hy)] = hd

init()
print(doGame())