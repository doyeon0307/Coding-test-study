n, m = map(int, input().split())
k = list(map(int, input().split()))

know = [0 for _ in range(n + 1)]
for i in range(1, k[0] + 1):
  know[k[i]] = 1

party = []

for _ in range(m):
  p = list(map(int, input().split()))
  party.append(p)
  
# 진실을 아는 사람의 겹지인 찾기
for _ in range(n):
  for p in party:
    has_friend = False
    for i in range(1, p[0] + 1):
      if know[p[i]]:
        has_friend = True
        break
    if has_friend:
      for j in range(1, p[0] + 1):
        know[p[j]] = 1

answer = 0
for p in party:
  can_lie = True
  for i in range(1, p[0] + 1):
    if know[p[i]]:
      can_lie = False
      break
  if can_lie:
    answer += 1

print(answer)
