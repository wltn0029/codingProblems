def solution(phone_book):
    front = {}
    for i in range(1, 21):
        front[i] = {}
    
    for p in phone_book :
        phoneLen = len(p)
        for i in range(1, phoneLen+1):
            if p[0:i] in front[i]:
                front[i][p[0:i]] += 1
            else :
                front[i][p[0:i]] = 1
        
    ans = True
    for p in phone_book :
        phoneLen = len(p)
        if p in front[phoneLen] and front[phoneLen][p] > 1:
            ans = False
            break
    return ans