import math

def solution(progresses, speeds):
    answer = []
    count = 0
    time = 0
    
    for p, s in zip(progresses, speeds):
        if time*s + p >= 100 :
            count +=1
        else :
            time = math.ceil((100-p)/s)
            if count>0 : answer.append(count)
            count = 1
            
    answer.append(count)
    return answer