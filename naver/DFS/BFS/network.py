from collections import deque 

def solution(n, computers):
    connected = [False] * n
    queue = deque()
    network = 0
    
    def bfs(start):
        queue.append(start)
        connected[start] = True
        while queue:
            cur = queue.popleft()
            for j, e in enumerate(computers[cur]):
                if e == 1 and not connected[j]:
                    queue.append(j)
                    connected[j] = True

    for i in range(n):
        if connected[i]:
            continue
        bfs(i)
        network += 1
        
    return network