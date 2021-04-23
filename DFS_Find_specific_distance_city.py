from collections import deque
# 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

# n : 도시 개수, m : 도로 개수
# 거리 정보(거리) : k, 출발 도시 번호 : x
# 최단 거리가 k인 모든 도시들의 번호 출력
n, m, k, x = map(int, input().split())

# 간선 정보
graph = [[] for _ in range(n+1)]
# [[], [2, 3], [3, 4], []]

for _ in range(m) :
	i, j = map(int, input().split())
	graph[i].append(j)

print(graph)

# graph[v]는 v와 연결된 노드 정보를 담고 있음
# n은 노드 개수
distance = [-1] * (n+1)
distance[x] = 0
# 0.   1.  2.  3.  4
# [0, -1, 1, 1, 2]
# q = [3]
q = deque([x])
while q :
	now = q.popleft()
	for next_node in graph[now] :
		if distance[next_node] == -1 :
			distance[next_node] = distance[now] + 1
			q.append(next_node)

for i in range(n+1) :
	if distance[i] == k :
		print(i)
if k not in distance :
	print(-1)