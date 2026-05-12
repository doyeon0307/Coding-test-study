def solution(citations):
    answer = 0
    
    citations.sort()
    start = 0
    end = citations[-1]

    while start <= end:
        h = (start + end) // 2
        idx = 0
        for i, c in enumerate(citations):
            if c >= h:
                idx = i
                break
        
        if len(citations) - idx >= h:
            start = h + 1
            if h > answer:
                print("find")
                answer = h
        else:
            end = h - 1    
    
    return answer