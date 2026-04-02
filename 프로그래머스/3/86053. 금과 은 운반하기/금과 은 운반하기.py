def solution(a, b, g, s, w, t):
    answer = -1
    
    n = len(g)
    max_t = 10 ** 16
    min_t = 0
    
    while min_t <= max_t:
        mid_t = (min_t + max_t) // 2
        gold = 0
        silver = 0
        total = 0
        for i in range(n):
            if g[i] == 0 and s[i] == 0:
                continue
            count = (mid_t // t[i]) // 2
            if mid_t - count * t[i] * 2 >= t[i]:
                count += 1
            total_w = count * w[i]
            total += min(total_w, g[i] + s[i])
            gold += min(total_w, g[i])
            silver += min(total_w, s[i])
        if gold >= a and silver >= b and total >= a + b:
            answer = mid_t
            max_t = mid_t - 1
        else:
            min_t = mid_t + 1  
    
    return answer