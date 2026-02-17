def solution(people, limit):
    answer = 0
    
    people.sort()
    
    min_idx = 0
    max_idx = len(people) - 1
    
    while min_idx <= max_idx:
        answer += 1
        if people[max_idx] + people[min_idx] <= limit:
            min_idx += 1
        max_idx -= 1
    
    return answer