from collections import deque

def solution(n, computers):
    answer = 0

    visited = [False] * n
    queue = deque()
    
    for s in range(n):
        if visited[s]:
            continue

        queue.append(s)
        visited[s] = True
        answer += 1

        while queue:
            c = queue.popleft()

            for i in range(n):
                if not visited[i] and (computers[c][i] or computers[i][c]):
                    queue.append(i)
                    visited[i] = True
    
    return answer