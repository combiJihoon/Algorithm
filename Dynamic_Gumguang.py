# import sys

# case 1
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7

# 19

# case 2
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

# 16

n, m = map(int, input().split())
temp = list(map(int, input().split()))

graph = [[0]*m for _ in range(n)]

k = 0
while k < len(temp) :
	for i in range(n) :
		for j in range(m) :
			graph[i][j] = temp[k]
			k += 1
			
print(graph)

# 오른쪽, 오른쪽 위, 오른쪽 아래로만 이동 가능
# 1 3 3 2
# 2 1 4 1
# 0 6 4 7

# i 는 x축, j는 y축
# x축 고정하고 y축만 이동한다.
for i in range(1, m) :
	for j in range(n) :
		left = left_down = left_up = 0
		# 왼쪽에서 옴(오른쪽 이동)
		if i-1 >= 0 :
			left = graph[j][i-1]

		# 왼쪽 아래에서 옴(오른쪽 위로 이동)
		if i-1 >= 0 and j+1 < n :
			left_down = graph[j+1][i-1]

		# 왼쪽 위에서 옴(오른쪽 아래로 이동)
		if i-1 >= 0 and j-1 >= 0 :
			left_up = graph[j-1][i-1]

		graph[j][i] +=  max(left, left_down, left_up)

# 마지막 열 중에 최댓값 출력
result = 0
for i in range(n) :
	result = max(result, graph[i][m-1])

print(result)
print(graph)

# 1 3 1 5
# 2 2 4 1
# 5 0 2 3
# 0 6 1 2

# 1 5 6 11
# 2 7 11 12
# 5 5 9 14
# 0 11 12 14