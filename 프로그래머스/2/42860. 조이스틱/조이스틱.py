def solution(name):
    answer = 0
    
    horizontal = 99
    vertical = 0

    for i in range(len(name) + 1):
        j = i + 1
        while j < len(name) and name[j] == 'A':
            j += 1
                
        k = i - 1
        while k > 0 and name[k] == 'A':
            k -= 1
        
        horizontal = min(horizontal, i * 2 + len(name) - j, (len(name) - i) * 2 + k)
        
    for s in name:
        vertical += min(ord(s) - ord('A'), ord('Z') - ord(s) + 1)
    
    return horizontal + vertical