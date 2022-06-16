def solution(participant, completion):
    partMap = {}
    for p in participant : 
        if p in partMap : 
            partMap[p] += 1
            continue
        partMap[p] = 1
    
    for c in completion:
        partMap[c] -= 1
        if partMap[c] == 0 : del partMap[c]
    
    ans = [k for k in partMap.keys()][0]
    return ans