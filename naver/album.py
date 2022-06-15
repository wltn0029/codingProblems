from functools import reduce

def solution(genres, plays):
    answer = []
    music = {}
    grs = []
    for i, p in enumerate(plays):
        if genres[i] in music : music[genres[i]].append((p, i))
        else : music[genres[i]] = [(p, i)]
    
    grs = sorted(music.keys(), key= lambda x : sum([p for p, i in music[x]]), reverse=True)
    for g in grs:
        p = sorted(music[g], key= lambda x: (x[0], -x[1]), reverse=True)
        answer.extend([i for p,i in p[0:min(2, len(p))]])
    
    return answer