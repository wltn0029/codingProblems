from collections import deque

def solution(prices):
    prices = deque([(p, i) for i, p in enumerate(prices)])
    prices.append((-1, len(prices)-1))
    monStack = [(-1, -1)]
    answer = []
    
    while prices :
        cur = prices.popleft()
        while monStack[-1][0] > cur[0] :
            e = monStack.pop()
            answer.append((cur[1]-e[1], e[1]))
        monStack.append(cur)
    
    return [a for a, i in sorted(answer, key = lambda x:x[1])]