# cy = ax + b
def make_line(xi, yi, xj, yj):
  if yi == yj:
    return [0, yi, 1]
  dx = xi - xj
  dy = yi - yj
  a = dy
  b = dx * yi - dy * xi
  c = dx
  return [a, b, c]

# (x, cy)가 y = ax + b를 지나거나 접하는가
def check_on_line(a, b, c, x, y):
  if c < 0:
    return c * y <= a * x + b  
  else:
    return c * y >= a * x + b

n = int(input())
b = list(map(int, input().split()))

answer = []

# i에서 보이는 건물의 개수 count
for i in range(n):
  count = 0
  # i에서 보이는 건물 후보
  for j in range(n):
    if i == j:
      continue
    # i와 j의 지붕을 잇는 선분
    params = make_line(i, b[i], j, b[j])
    # 선분과 겹치는 건물이 있다면 can_see는 False
    can_see = True
    if i < j:
      for k in range(i + 1, j):
        if check_on_line(params[0], params[1], params[2], k, b[k]):
          can_see = False
          break
    else:
      for k in range(j + 1, i):
        if check_on_line(params[0], params[1], params[2], k, b[k]):
          can_see = False
          break
    # i에서 j를 볼 수 있음
    if can_see:
      count += 1

  answer.append(count)

print(max(answer))