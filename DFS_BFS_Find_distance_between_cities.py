from collections import deque
import sys
# n : 도시의 개수, m : 도로의 개수, k : 거리 정보, x : 출발 도시 번호
input = sys.stdin.readline

def bfs(x, answer) :
	q = deque()
	q.append(x)
	while q :
		new = q.popleft()
		for i in graph[new] :
			if answer[i] == 100 :
				# 이동
				answer[i] = answer[new]+1
				q.append(i)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
	i, j = map(int, input().split())
	graph[i].append(j)

# 작은 값만을 넣는다.
answer = [-1] * (n+1)
answer[x] = 0
# 실행
bfs(x, answer)

isNone = False
for i in range(len(answer)) :
	if answer[i] == k :
		print(i)
		isNone = True

if not isNone :
	print(-1)