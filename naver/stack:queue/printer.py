from collections import deque

def solution(priorities, location):
    answer = 1
    pri = deque()
    for i, p in enumerate(priorities):
        pri.append((p, i))
    
    while len(pri) > 0:
        mv = pri.index(max(pri, key =lambda x : x[0]))
        pri.rotate(-mv)
        if pri[0][1] == location : 
            break
        pri.popleft()
        answer+=1
    return answer