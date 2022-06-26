def solution(numbers, target):
    ans = 0
    M = (sum(numbers)-target)/2
    n = len(numbers)
    
    for i in range(1, 2**n):
        cur = 0
        curSum = 0
        while i > 0:
            if i&1 : 
                curSum += numbers[cur]
            cur += 1
            i >>=1
        if curSum == M :
            ans += 1
    return ans