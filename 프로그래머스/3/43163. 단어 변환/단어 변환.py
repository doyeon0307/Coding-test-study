from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    bfs = deque([[-1, 0]])
    
    while bfs:
        l = bfs.popleft()
        b = ""
        if l[0] < 0:
            b = begin
        else:
            b = words[l[0]]
            
        if b == target:
            return l[1]
        
        for i, w in enumerate(words):
            cnt = 0
            for j in range(len(w)):
                if b[j] != w[j]:
                    cnt += 1
            if cnt == 1:
                bfs.append([i, l[1] + 1])
    
    return 0