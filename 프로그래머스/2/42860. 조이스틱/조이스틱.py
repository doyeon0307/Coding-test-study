def solution(name):
    answer = 0
    
    n = len(name)
    
    # 상하 최소 움직임 수
    for c in name:
        answer += min(ord(c) - 65, 90 - ord(c) + 1)
    
    # 좌우 최소 움직임 수
    move = n - 1
    
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == "A":
            next_i += 1
        
        move = min(
            move, 
            i * 2 + n - next_i,
            (n - next_i) * 2 + i
        )
        
    return answer + move
