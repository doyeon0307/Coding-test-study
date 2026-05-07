def solution(priorities, location):
    answer = 0

    start = 0
    end = len(priorities) - 1
    target = location
    
    while(start <= end):
        s = priorities[start]

        if s == max(priorities[start:]):
            answer += 1
            if start == target:
                return answer
            
        else:
            priorities.append(s)
            end += 1
            if start == target:
                target = end
            
        start += 1

    return answer