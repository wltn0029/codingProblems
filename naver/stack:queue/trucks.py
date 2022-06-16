from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0 for i in range(bridge_length)])
    weight_sum = 0
    
    while len(trucks) != 0:
        f = bridge.popleft()
        n = 0
        weight_sum -= f
        if len(trucks) != 0 and trucks[0] + weight_sum <= weight:
            n = trucks.popleft()
        bridge.appendleft(n)
        weight_sum += n
        bridge.rotate(-1)
        answer+=1
        
    return answer + bridge_length