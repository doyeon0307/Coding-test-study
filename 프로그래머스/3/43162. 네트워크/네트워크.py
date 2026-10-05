from collections import deque

def solution(n, computers):
    answer = 0
    v = [0] * n
    
    for c in range(n):
        if v[c]:
            continue
        
        bfs = deque([c])

        while bfs:
            l = bfs.popleft()
            if not v[l]:
                v[l] = 1
                near = computers[l]
                for i, n in enumerate(near):
                    if n and not v[i]:
                        bfs.append(i)
        
        answer += 1
    
    return answer