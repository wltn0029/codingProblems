from itertools import product

def solution(numbers, target):
    numbers = [(x, -x) for x in numbers]
    e = list(map(sum,product(*numbers)))
    return e.count(target)
