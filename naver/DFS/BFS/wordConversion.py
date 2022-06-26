from collections import deque 

def solution(begin, target, words):
    if not (target in words) : 
        return 0
    
    deq = deque()
    changable = {} # index : list of index
    words.append(begin)
    visited = [False]*len(words)
    wordLen = len(begin)
    
    # fill changable 
    for i, cur in enumerate(words):
        able = []
        for j, cmp in enumerate(words):
            diff=0
            for w in range(wordLen):
                if cur[w] != cmp[w] : diff+=1
            if diff == 1 : able.append(j)
        changable[i] = able
    
    # bfs 
    deq.append((len(words)-1,0))
    visited[len(words)-1] = True
    while deq :
        cur, level = deq.popleft()
        visited[cur] = True
        if words[cur] == target :
            return level
        for cand in changable[cur]:
            if visited[cand] : continue
            deq.append((cand, level+1))
            
    return 0