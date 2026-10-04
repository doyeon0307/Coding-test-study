from collections import deque 

def solution(bridge_length, weight, truck_weights):
    answer = 0
    i = 0
    
    que = deque([0 for _ in range(bridge_length)])
    
    while i < len(truck_weights):
        answer += 1
        if len(que) == bridge_length:
            que.pop()
        
        if truck_weights[i] + sum(que) <= weight:
            que.appendleft(truck_weights[i])
            i += 1
        else:
            que.appendleft(0)
    
    while que:
        answer += 1
        que.pop()
        if sum(que) == 0:
            break
    
    return answer