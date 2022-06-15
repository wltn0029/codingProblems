def solution(clothes):
    answer = 1
    closet = {}
    for c, t in clothes :
        if t in closet : closet[t] += 1
        else : closet[t] = 1
    for c in closet :
        answer *= (closet[c]+1)
    answer -= 1
    return answer