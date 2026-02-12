answer = 0

def sumOrSub(i, numbers, result, target):
    global answer
    if i >= len(numbers):
        if result == target:
            answer += 1
        return
    
    sumOrSub(i + 1, numbers, result + numbers[i], target)
    sumOrSub(i + 1, numbers, result - numbers[i], target)

def solution(numbers, target):
    global answer
    sumOrSub(0, numbers, 0, target)
    
    return answer