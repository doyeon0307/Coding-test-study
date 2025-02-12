N = int(input())
tree = list(map(int, input().split()))
delete = int(input())

# 삭제
def delete_node(d):
  # d를 부모로 갖는 노드 삭제
  for n, t in enumerate(tree):
    if t == d:
      tree[n] = -2
      delete_node(n)

# 자기 자신 삭제
tree[delete] = -2

# 자식 노드 삭제
delete_node(delete)

# 리프 노드 개수
answer = 0
for i, t in enumerate(tree):
  if t > -2:
    has_child = False
    for n in tree:
      if i == n:
        has_child = True
        break
    if not has_child:
      answer += 1

print(answer)