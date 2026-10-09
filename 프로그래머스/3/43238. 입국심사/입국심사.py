def solution(n, times):
    answer = 0
    
    s = min(times)
    e = max(times) * n
    
    while s <= e:
        m = (s + e) // 2
        c = 0
        for t in times:
            c += m // t
        if c >= n:
            e = m - 1
        else:
            s = m + 1
    
    return s