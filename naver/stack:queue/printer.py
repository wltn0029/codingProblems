from collections import deque

def solution(priorities, location):
    answer = 0
    pri = deque([(p,i) for i, p in enumerate(priorities)])
    
    while len(pri) > 0:
        mv = pri.index(max(pri, key =lambda x : x[0]))
        pri.rotate(-mv)
        p, o = pri.popleft()
        answer+=1
        if o == location : 
            break
    return answer