from functools import reduce

def solution(genres, plays):
    answer = []
    music = {}
    s = []
    for i, p in enumerate(plays):
        if genres[i] in music : music[genres[i]].append((p, -i))
        else : music[genres[i]] = [(p, -i)]
    
    for k in music :
        s.append((reduce(lambda acc, cur: acc+cur[0], music[k], 0), k))
        music[k].sort(reverse=True)

    s.sort(reverse=True)
    print(s)
    for sm, g in s:
        if len(music[g]) <2 : answer.append(-music[g][0][1])
        else : answer.extend([-i for p, i in music[g][0:2]])
    
    return answer