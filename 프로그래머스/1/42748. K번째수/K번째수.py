def solution(array, commands):
    answer = []
    
    for c in commands:
        a, b, c = map(int, c)
        answer.append(sorted(array[a-1:b])[c-1])
    
    return answer