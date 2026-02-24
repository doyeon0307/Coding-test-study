def solution(name):
    answer = 0
    
    size = len(name)
    
    for n in name:
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
    
    move = size - 1
    for i in range(size):
        next_i = i + 1
        while next_i < size:
            if name[next_i] == 'A':
                next_i += 1
            else:
                break

        move = min(move, i * 2 + size - next_i, (size - next_i) * 2 + i)
        
    return answer + move
