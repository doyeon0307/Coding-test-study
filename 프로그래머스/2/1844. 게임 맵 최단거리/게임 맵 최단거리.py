from collections import deque

def con(maps, row, column,a, b):
    if a < 0 or b < 0 or a >= row or b >= column:
        return -1
    if maps[a][b]:
        return a * column + b
    else:
        return -1

def solution(maps):
    answer = 0
    row = len(maps)
    column = len(maps[0])
    
    bfs = deque([0])
    v = [0] * row * column
    v[0] = 1
    
    while bfs:
        l = bfs.popleft()
        if l == row * column - 1:
            answer = v[l]
            break
        
        x, y = l // column, l % column
        near = [con(maps, row, column, x + 1, y), con(maps, row, column, x - 1, y), con(maps, row, column, x, y + 1), con(maps, row, column, x, y - 1)]
        for n in near:
            if n >= 0 and not v[n]:
                bfs.append(n)
                v[n] = v[l] + 1
    
    if not answer:
        answer = -1

    return answer