n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


# 위에서 내려오는 경우, 왼쪽 위에서 내려오는 경우
for i in range(1, n):
    for j in range(i+1):
        # 바로 위에서 내려오는 경우
        if i == j:
            up = 0
        else:
            up = graph[i-1][j]

        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            left_up = 0
        else:
            left_up = graph[i-1][j-1]

        plus = max(up, left_up)
        graph[i][j] += plus

print(max(graph[n-1]))
