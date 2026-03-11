def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    
    for i in range(1, yellow // 2 + 1):
        if yellow % i != 0:
            continue
        x, y = yellow // i, i
        b = (x + y + 2) * 2
        if b == brown:
            return [x + 2, y + 2]
    
    return []