import copy

n, m, h = list(map(int, input().split()))
ladder = [[0]*(n-1) for i in range(h)]
ans = -1 

for i in range(m):
    l, k = list(map(int, input().split()))
    ladder[l-1][k-1] = 1

def calculateAddition(l) :
    one = []
    two = []
    cur = 0
    next = 0
    evenCond = False
    for i in range(n-1):
        evenCond = False
        cur = 0
        while cur<h:
            if l[cur][i] == 1 :
                if not evenCond: 
                    evenCond = True
                    next = 0
                else :
                    evenCond = False
                    if next % 2 != 0 : two.append(i)
            else :
                if evenCond :
                    if i<n-2 and l[cur][i+1] == 1:
                        next +=1 
            cur += 1
        if evenCond : one.append(i)

    # print(one, two)
    twoI = 0
    while twoI < len(two):
        cur = two[twoI]
        if (cur+1) in one :
            two.remove(cur)
            continue
        twoI += 1

    threeToOneCond = len(two) == 2 and (two[0] +1) == two[1] 
    twoLen = 1 if threeToOneCond else len(two)
    if 2*twoLen + len(one) > 3 : return None

    if len(two) == 1 : two.append(two[0]+1)
    elif threeToOneCond : two = [two[1]]

    stack = []
    for i in two : stack.append([i, i])
    if len(stack) == 0 and len(one) > 0 : stack = [[]]
    for i in one :
        for j in stack:
            j.append(i)
    return stack 

def dfs(l, level, stack) :
    global ans
    if level == len(stack) : 
        result = calculateAddition(l)
        if result != None and len(result) == 0 : 
            ans = level
        return
    if ans != -1 : return

    next = stack[level]
    for i in range(h): 
        if l[i][next] == 1 : continue
        elif 1 < next and l[i][next-1] == 1 : continue
        elif next < n-2 and l[i][next+1] == 1 : continue
        nl = copy.deepcopy(l)
        nl[i][next] = 1
        dfs(nl, level+1, stack)

stack = calculateAddition(ladder)
if stack == None : print(ans)
elif len(stack) == 0 : print(0)
else :
    for i in range(len(stack)):
        dfs(ladder, 0, stack[i])

    print(ans)