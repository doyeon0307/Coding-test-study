n, l = map(int, input().split())
pipes = sorted(list(map(int, input().split())))

answer = 0

# 테이프 끝 지점
tape = pipes[0] - 0.5

for p in pipes:
    # 테이프 필요
    if p + 0.5 > tape:
        answer += 1
        tape = p - 0.5 + l
    
print(answer)
