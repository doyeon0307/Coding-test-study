def solution(n, lost, reserve):
    answer = 0
    
    two_but_lost = []
    for l in lost:
        if l in reserve:
            two_but_lost.append(l)
    
    for t in two_but_lost:
        lost.remove(t)
        reserve.remove(t)
            
    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
        
    return  n - len(lost)