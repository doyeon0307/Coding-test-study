def solution(n, wires):
    answer = 100000000
    
    con = [[] for _ in range(n + 1)]
    for w in wires:
        a, b = map(int, w)
        con[a].append(b)
        con[b].append(a)

    for w in wires:
        a, b = map(int, w)
        con[a].remove(b)
        con[b].remove(a)

        stack = [a]
        tree = {a}
           
        while stack:
            l = stack.pop()
            for i in con[l]:
                if not (i in tree):
                    stack.append(i)
                    tree.add(i)
        
        con[a].append(b)
        con[b].append(a)

        answer = min(answer, abs(n - len(tree) * 2))
        
    return answer