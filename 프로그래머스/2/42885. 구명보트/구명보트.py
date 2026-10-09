def solution(people, limit):
    answer = len(people)
    
    minimum = len(people) - 1
    people.sort(reverse = True)
    
    for i, p in enumerate(people):
        if minimum > i and p + people[minimum] <= limit:
            minimum -= 1
            answer -= 1
    
    return answer