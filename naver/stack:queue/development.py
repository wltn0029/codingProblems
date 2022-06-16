from collections import deque
import math

def solution(progresses, speeds):
    prog = deque(progresses)
    sp = deque(speeds)
    answer = []
    
    while len(prog) != 0 :
        x = math.ceil((100-prog[0])/sp[0])
        for i, p in enumerate(prog):
            prog[i] = min(100, p+sp[i]*x)
        num = 0
        while len(prog)>0 and prog[0] >= 100 :
            prog.popleft()
            sp.popleft()
            num += 1
        answer.append(num)
    
    return answer