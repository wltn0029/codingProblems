import copy

n, m, h = list(map(int, input().split()))
ladder = [[0]*(n-1) for i in range(h)]
ans = -1

for i in range(m):
    l, k = list(map(int, input().split()))
    ladder[l-1][k-1] = 1

def checkPossible():
    ans = True
    for i in range(n):
        cur = i
        for j in range(h):
            if 0<cur and ladder[j][cur-1] == 1 : cur -= 1
            elif cur<n-1 and ladder[j][cur] == 1 : cur += 1
        if cur != i :
            ans = False
            break
    
    return ans

def dfs(x, y, level, end) :
    global ans
    if checkPossible() : 
        ans = level
        return
    if level == end or ans != -1 : return

    for i in range(x, h):
        startI = 0 if i > x else y+1
        for j in range(startI, n-1):
            if ladder[i][j] == 1 or \
                (1<j and ladder[i][j-1] == 1) or (j<n-2 and ladder[i][j+1] == 1) : continue
            ladder[i][j] = 1
            dfs(i, j, level+1, end)
            ladder[i][j] = 0

for i in range(4):
    dfs(-1, -1, 0, i)
    if ans != -1 : break
print(ans)