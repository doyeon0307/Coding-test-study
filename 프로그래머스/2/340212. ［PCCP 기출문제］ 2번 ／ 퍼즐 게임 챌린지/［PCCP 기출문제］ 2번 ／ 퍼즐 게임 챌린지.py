def solution(diffs, times, limit):
    answer = 0
    
    minLevel = 1
    maxLevel = max(diffs)
    
    while minLevel <= maxLevel:
        level = (minLevel + maxLevel) // 2
        time = 0
        
        for i, d in enumerate(diffs):
            time += times[i]
            if d > level:
                prev = times[i - 1] if i > 0 else 0
                time += (d - level) * (prev + times[i])
        
        if time <= limit:
            answer = level
            maxLevel = level - 1
        else:
            minLevel = level + 1
    
    return answer