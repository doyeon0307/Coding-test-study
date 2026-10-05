from collections import deque

def solution(n, computers):
    answer = 0
    v = [0] * n
    
    for c in range(n):
        if v[c]:
            continue
        
        dfs = deque([c])

        while dfs:
            l = dfs.popleft()
            if not v[l]:
                v[l] = 1
                near = computers[l]
                for i, n in enumerate(near):
                    if n and not v[i]:
                        dfs.append(i)
        
        answer += 1    
    
    return answer