# 인구 수가 주어졌을 때 인구 이동 몇 번 발생하는 지 
# r행 c열
from collections import deque

# n by n 크기의 땅, l <= 인구 수 <= r
n, l, r = map(int, input().split())
# 나라별 인구 수
graph = []
# 방문 여부
visited = []
# 연합할 나라들의 인구수 배열
toBeCombinated = []
for _ in range(n) :
	graph.append(list(map(int, input().split())))
	# 방문 여부 확인
	visited.append([0 for i in range(n)])
	# 연합할 국가들 리스트
	toBeCombinated.append([0 for i in range(n)])

answer = 0

def solution(x, y) :	
	global answer
	# q에서 나온 뒤
	while True :
		nearestChecker(x, y)
		changedNum = numOfPeople()
		if not changedNum :
			break
		else :
			answer += 1
			clearChange(changedNum)
	return answer	

# 현재 위치 인덱스 : x, y
# 상하좌우 돌며 확인
def nearestChecker(x, y) :
	global visited
	global toBeCombinated

	q = deque()
	q.append((x, y))

	dx = [1, -1, 0, 0] # 행
	dy = [0, 0, -1, 1] # 열

	while q :
		x, y = q.popleft()
		if visited[x][y] == 0 :
			visited[x][y] = 1
			# 주변 탐색 진행
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1 :
				if visited[nx][ny] == 0 :
					q.append((nx, ny))
					# True면 연합할 나라의 인구 수 추가하기
					if numDiffChecker(x, y, nx, ny) :
						if toBeCombinated[x][y] == 0 :
							toBeCombinated[x][y] = graph[x][y]
						if toBeCombinated[nx][ny] == 0 :
							toBeCombinated[nx][ny] = graph[nx][ny]

# 인구 수 차이가 l과 r 사이인지 체크
# x, y 는 위치 인덱스
def numDiffChecker(x, y, nx, ny) :
	global graph
	numDiff = abs(graph[x][y] - graph[nx][ny])
	if l <= numDiff  <= r :
		return True
	return False

# 연합한 나라들의 총 변화한 인구 수
def numOfPeople() :
	# 연합 나라 수 
	count = 0
	# 연합 나라 들의 총 인구 수
	totalNum = 0
	for i in range(n) :
		for j in range(n) :
			if toBeCombinated[i][j] != 0 :
				count += 1
				totalNum += toBeCombinated[i][j]
	if count == 0 :
		return False
	else :
		return totalNum // count

# graph 다시 채우기
def clearChange(changedNum) :
	global graph
	global toBeCombinated

	for i in range(n) :
		for j in range(n) :
			if toBeCombinated[i][j] != 0 :
				graph[i][j] = changedNum
				# 연합에 참여했던 국가들 다시 제거
				toBeCombinated[i][j] = 0 

print(solution(0, 0))