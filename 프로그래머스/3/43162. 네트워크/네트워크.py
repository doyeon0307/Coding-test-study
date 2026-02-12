from collections import deque

def solution(n, computers):
    answer = n

    visited = [False] * n
    queue = deque()
    
    for s in range(n):
        if visited[s]:
            continue

        queue.append(s)
        visited[s] = True
        count = 1

        while queue:
            c = queue.popleft()

            for i in range(n):
                if not visited[i] and (computers[c][i] or computers[i][c]):
                    count += 1
                    queue.append(i)
                    visited[i] = True

        answer = answer - count + 1
    
    return answer