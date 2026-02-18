def solution(number, k):
    answer = ''
    
    stack = []
    max_stack = len(number) - k
    
    for n in number:
        if k <= 0:
            stack.append(n)
            continue
        
        if not stack:
            stack.append(n)
            continue
        
        while stack:
            prev = stack.pop()
            if n > prev:
                k -= 1
                if k <= 0:
                    break
                continue
            else:
                stack.append(prev)
                break
                
        stack.append(n)

                
    for s in stack[:max_stack]:
        answer += s
    
    return answer