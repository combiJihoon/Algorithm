from itertools import combinations as cb
from copy import deepcopy

n = int(input())
graph = []
for _ in range(n) :
	graph.append(list(input().split()))


# 가능한 obstacles, 학생, 선생님 위치 확인
nothing = []
students = []
teachers = []
for i in range(n) :
	for j in range(n) :
		if graph[i][j] == 'X' :
			nothing.append((i, j))
		elif graph[i][j] == 'S' :
			students.append((i, j))
		elif graph[i][j] == 'T' :
			teachers.append((i, j))
ob_index = []
ob_index += cb(nothing, 3)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# T로 전염 -> S가 닿으면 No를 리턴
def dfs(temp_graph, x, y, i) :
	global dx, dy
	if 0 <= x <= n-1 and 0 <= y <= n-1 and  	temp_graph[x][y] != "O" :
		temp_graph[x][y] = "T"
		nx = x + dx[i]
		ny = y + dy[i]
		dfs(temp_graph, nx, ny, i)
	else :
		return

def check() :
	for (x, y) in teachers :
		for i in range(4) :
			dfs(temp_graph, x, y, i)
	for (x, y) in students :
		if temp_graph[x][y] != "S" :
			return False
	return True

is_true = True
for case in list(cb(nothing, 3)) :
	temp_graph = deepcopy(graph)
	# O로 채워놓기
	for (x, y) in case :
		temp_graph[x][y] = "O"
	if check() :
		print("YES")
		is_true = False
		break
	# 원상복귀
	# for (x, y) in case :
	# 	temp_graph[x][y] = "X"
if is_true :
	print("NO") 