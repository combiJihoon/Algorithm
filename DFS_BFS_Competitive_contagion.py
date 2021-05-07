import sys
from collections import deque

input = sys.stdin.readline

# n : size of the graph, k : type if viruses
n, k = map(int, input().split())

graph = []
virus = []   # virus의 종류와 인덱스 리스트
for i in range(n) :
	graph.append(list(map(int, input().split())))
	for j in range(n) :
		if graph[i][j] != 0 :
			# virus 리스트에 graph의 값과 인덱스 추가
			virus.append((graph[i][j], i, j, 0))

s, X, Y = map(int, input().split())


def bfs(s, X, Y) :
	count = 0
	q = deque(virus)

	# x : 행, y : 열
	dx = [1, -1, 0, 0]
	dy = [0, 0, -1, 1]

	while q :
		prev, x, y, count = q.popleft()
		if count == s :
			break 
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx <= n-1 and 0 <= ny <= n-1 :
				if graph[nx][ny] == 0 :
					graph[nx][ny] = graph[x][y]
					q.append((graph[nx][ny], nx, ny, count + 1))
				
	return graph[X-1][Y-1]

print(bfs(s, X, Y))

