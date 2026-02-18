def solution(number, k):
    answer = ''
    
    stack = []
    
    for n in number:
        while stack and k > 0 and n > stack[-1]:
            stack.pop()
            k -= 1 
        stack.append(n)

    if k > 0:
        stack = stack[:-k]
        
    for s in stack:
        answer += s
    
    return answer