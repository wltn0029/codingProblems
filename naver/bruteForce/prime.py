from itertools import permutations
import math 

def solution(numbers):
    perms = set()
    for i in range(1, len(numbers)+1):
        perms|= set(map(int, map("".join, permutations(numbers, i))))
    largest = max(perms)
    
    perms-=set((0,1))
    for i in range(2, int(math.sqrt(largest))+1):
        perms-=set(range(i*2, largest+1, i))

    return len(perms)