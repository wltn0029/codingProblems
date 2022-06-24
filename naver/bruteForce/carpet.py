def solution(brown, yellow):
    factors = []
    h, w = 0, 0
    for i in range(1, int(yellow**(1/2)) + 1):
        if yellow%i == 0 : factors.append((i, yellow//i))
    
    for h, w in factors:
        if (2 *(h+w)+4) == brown :
            break
            
    return [w+2, h+2]
    