from collections import Counter
from functools import reduce

def solution(clothes):
    answer = 1
    c = Counter([kind for cloth, kind in clothes])
    print(c)
    answer = reduce(lambda acc, cur : acc * (c[cur]+1), c, 1)
    return answer-1