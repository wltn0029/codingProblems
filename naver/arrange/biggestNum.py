from functools import reduce, cmp_to_key

def sortFunc(x,y):
    if x+y > y+x : return 1
    elif x+y < y+x : return -1
    else : return 0

def solution(numbers):
    sortNum = list(map(str, numbers))
    sortNum.sort(key=cmp_to_key(sortFunc), reverse=True) 
    ans = reduce(lambda acc, cur: acc+cur,sortNum,"")
    if int(ans) == 0 : ans = "0"
    return ans