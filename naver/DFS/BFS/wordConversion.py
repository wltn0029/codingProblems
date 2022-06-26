from collections import deque 

def gen_adjacent(cur, words):
    for w in words:
        diff = 0 
        for c, cmp in zip(cur, w):
            if c != cmp : diff+=1
        if diff == 1 :
            yield w

def solution(begin, target, words):
    if not (target in words) : 
        return 0
    
    deq = deque([begin])
    dist = {begin : 0}
    
    # bfs 
    while deq :
        cur = deq.popleft()
        if cur == target : return dist[cur]
        for cand in gen_adjacent(cur, words):
            if cand in dist : continue
            deq.append(cand)
            dist[cand] = dist[cur]+1
            
    return 0