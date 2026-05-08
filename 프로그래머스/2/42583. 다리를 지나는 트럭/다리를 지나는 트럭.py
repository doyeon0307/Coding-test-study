from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque()
    for _ in range(bridge_length):
        bridge.append(0)
    
    cur_idx = 0
    max_idx = len(truck_weights) - 1
    
    while bridge:
        answer += 1
        bridge.popleft()
        
        if cur_idx <= max_idx:
            w = truck_weights[cur_idx]
            if sum(bridge) + w <= weight:
                bridge.append(w)
                cur_idx += 1
            else:
                bridge.append(0)
        
    return answer