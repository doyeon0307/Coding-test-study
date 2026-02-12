from collections import deque

def solution(maps):
    answer = -1
    
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()    
    mark = maps
    
    queue.append([0, 0, 1])
    mark[0][0] = 0

    while queue:
        x, y, c = map(int, queue.popleft())

        # 성공
        if (x == n - 1 and y == m - 1):
            answer = c
            break
        
        # 동쪽
        if y + 1 < m and mark[x][y + 1]:
            queue.append([x, y + 1, c + 1])
            mark[x][y + 1] = 0
        # 서쪽
        if y - 1 >= 0 and mark[x][y - 1]:
            queue.append([x, y - 1, c + 1])
            mark[x][y - 1] = 0
        # 남쪽
        if x + 1 < n and mark[x + 1][y]:
            queue.append([x + 1, y, c + 1])
            mark[x + 1][y] = 0
        # 북쪽
        if (x - 1 >= 0 and mark[x - 1][y]):
            queue.append([x - 1, y, c + 1])
            mark[x - 1][y] = 0

    return answer