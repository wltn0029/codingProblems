def solution(answers):
    one = [1,2, 3, 4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    answer = [[0,1], [0,2], [0,3]]
    
    for i, a in enumerate(answers):
        if a == one[i%5] : answer[0][0] +=1 
        if a == two[i%8] : answer[1][0] +=1
        if a== three[i%10] : answer[2][0] +=1
    
    answer.sort(key=lambda x:x[0], reverse=True)
    return [i for a, i in answer if a == answer[0][0]]