def solution(sizes):
    answer = 0
    
    max_first = 0
    max_second = 0
    
    for s in sizes:
        f, s = map(int, sorted(s))
        
        max_first = max(max_first, f)
        max_second = max(max_second, s)
    
    return max_first * max_second