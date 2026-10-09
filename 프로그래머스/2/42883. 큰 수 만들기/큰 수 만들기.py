def solution(number, k):
    answer = ''
    
    stack = []
    
    for n in number:
        if not stack:
            stack.append(n)
        else:
            while k > 0 and stack and stack[-1] < n:
                stack.pop()
                k -= 1
            stack.append(n)
    
    if k > 0:
        stack = stack[:-k]
    
    for s in stack:
        answer += s
    
    return answer