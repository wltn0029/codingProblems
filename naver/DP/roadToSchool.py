def solution(m, n, puddles):
    maxNum = 1000000007
    
    path = [0]*(m+1)
    path[1] = 1 
    for i in range(1, n+1):
        for j in range(1, m+1):
            path[j] = 0 if [j,i] in puddles else (path[j] + path[j-1])%maxNum
            
    return path[m]