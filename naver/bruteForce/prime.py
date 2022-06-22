from itertools import permutations
import math 

def solution(numbers):
    nums = list(numbers)
    perms = set()
    answer = 0
    for i in range(1, len(nums)+1):
        for npairs in permutations(nums, i) :
            num = ""
            for n in npairs: num+=n
            perms.add(int(num))
    largest = max(perms)
    
    prime = [True for _ in range(0,largest+1)]
    prime[1] = False
    prime[0] = False
    for i in range(2, int(math.sqrt(largest))+1):
        if prime[i] == True:
            j = 2
            while i*j <= largest :
                prime[i*j] = False
                j += 1
    
    for num in perms :
        if prime[num] :
            print(num)
            answer+=1
    return answer