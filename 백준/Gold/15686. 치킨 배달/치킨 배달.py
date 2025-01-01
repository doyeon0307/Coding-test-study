from itertools import combinations

def get_minimum_city_chicken_distance(houses, chickens, m):
  # 남길 치킨집들
  left = []
  for x in range(m):
    left.extend(list(combinations(chickens, x + 1)))
  
  # 살아남을 치킨집 중 최소 치킨 거리 구하기기
  minimum_city_chicken_distance = 1000000000000
  for l in left:
    result = get_city_chicken_distance(houses, l)
    if (result < minimum_city_chicken_distance):
      minimum_city_chicken_distance = result

  return minimum_city_chicken_distance


# 도시 치킨 거리 계산
def get_city_chicken_distance(houses, chickens):
  minimum_city_distance = 0
  for h in houses:
    minimum_house_distance = 1000000000000
    for c in chickens:
      result = get_chicken_distance(h, c)
      if result < minimum_house_distance:
        minimum_house_distance = result
    minimum_city_distance += minimum_house_distance

  return minimum_city_distance

# 거리 계산
def get_chicken_distance(house, chicken):
  return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


n, m = map(int, input().split())

# 집 좌표
houses = []

# 치킨 집 좌표
chickens = []

for i in range(n):
  row = map(int, input().split())
  for index, r in enumerate(row):
    if r == 1:
      houses.append((i, index))
    elif r == 2:
      chickens.append((i, index))

# 치킨 집이 이미 m개 이하인 경우
if chickens.__len__() < m:
  print(get_city_chicken_distance(houses, chickens))

# 치킨 집이 m개 초과인 경우 -> m개 이하로 줄여야 함
else:
  print(get_minimum_city_chicken_distance(houses, chickens, m))