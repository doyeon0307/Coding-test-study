from collections import deque

def solution(n, edge):
    answer = 0
    
    g = [[] for _ in range(n + 1)]
    
    for e in edge:
        a, b = map(int, e)
        g[a].append(b)
        g[b].append(a)
        
    visited = [0 for _ in range(n + 1)]

    bfs = deque([1])
    visited[1] = 1

    while bfs:
        n = bfs.popleft()
        
        for m in g[n]:
            if visited[m] == 0:
                bfs.append(m)
                visited[m] = visited[n] + 1
    
    visited[1] = 0

    m = max(visited)
    for v in visited:
        if v == m:
            answer += 1
    
    return answer