def solution(answers):
    pattern1 =[1,2, 3, 4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    answer = [0, 0, 0]
    
    for i, a in enumerate(answers):
        if a == pattern1[i%5] : answer[0] +=1 
        if a == pattern2[i%8] : answer[1] +=1
        if a== pattern3[i%10] : answer[2] +=1
        
    mv = max(answer)
    return [i+1 for i,a in enumerate(answer) if a == mv]