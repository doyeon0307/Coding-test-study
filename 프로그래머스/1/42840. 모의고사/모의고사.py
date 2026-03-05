def solution(answers):
    answer = []
    
    scores = [0 for _ in range(3)]
    
    f_pattern = [5, 1, 2, 3, 4]
    s_pattern = [5, 2, 1, 2, 3, 2, 4, 2]
    t_pattern = [5, 3, 3, 1, 1, 2, 2, 4, 4, 5]
    
    f_len = len(f_pattern) # 5
    s_len = len(s_pattern) # 8
    t_len = len(t_pattern) # 10
    
    for i, a in enumerate(answers):
        i += 1
        if f_pattern[i % f_len] == a:
            scores[0] += 1
        if s_pattern[i % s_len] == a:
            scores[1] += 1
        if t_pattern[i % t_len] == a:
            scores[2] += 1
    
    m_score = max(scores)
    
    for i, s in enumerate(scores):
        if s == m_score:
            answer.append(i + 1)
    
    return answer