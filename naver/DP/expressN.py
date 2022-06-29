from collections import defaultdict
from itertools import product
from functools import reduce

def solution(N, number):
    dp = defaultdict(set)
    dp[1].add(N)
    
    for n in range(2,9):
        dp[n].add(int(reduce(lambda acc, cur: acc+cur, [str(N)]*n, "")))
        for i in range(1, n):
            left = dp[i]
            right = dp[n-i]
            for l, r in product(left,right):
                if r != 0 : dp[n].add(l/r)
                dp[n].add(l*r)
                dp[n].add(l+r)
                dp[n].add(l-r)
        
    
    for i in range(1,9):
        if number in dp[i]:
            return i
    return -1