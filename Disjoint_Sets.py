# 개념 소스코드

import time

start_time = time.time()

# 특정 원소가 속한 집합 찾기 
def find_parent(parent, x) :
  # 루트 노드가 아니라면 루트 노드 찾을 때까지 재귀적으로 호출
  if parent[x] != x :
    return find_parent(parent, parent[x])
  # parent 리스트에 나 자신을 넣었을 때 나 자신이 나온다면 루트 노드가 나 자신으로 만들어진 '초기 상태'
  return x

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

# 노드의 개수와 간선 개수(union 연산의 개수) 입력 받기
v, e = map(int, input().split())
# 부모 테이블 0으로 초기화(노드의 개수+1 만큼)
parent = [0] * (v+1) 

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1) :
  parent[i] = i

# union 연산을 각각 수행(간선의 개수만큼)
for i in range(e) :
  # a, b를 union(합집합) 연산하라는 뜻
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속한 집합 출력 : 루트노드(부모노드)가 출력된다.
print('각 원소가 속한 집합(루트노드) : ', end = '')
for i in range(1, v+1) :
  print(find_parent(parent, i), end = ' ')

print()

# 부모 테이블 내용 출력 : 완전 부모는 아니고 임시 부모 정도로 볼 수 있다
# -> 진짜 부모는 계속 거쳐가야 알 수 있으며 위의 각 원소가 속한 집합이 진짜 부모!
print('부모 테이블 : ', end = '')
for i in range(1, v+1) :
  print(parent[i], end = ' ')

end_time = time.time()
print()
print(end_time - start_time)
