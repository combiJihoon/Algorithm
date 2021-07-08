from collections import deque


def hideAndSeek(n, k):
    q = deque()
    q.append(n)

    visited = [0] * 100001

    while q:
        x = q.popleft()
        if x == k:
            return visited[k]

        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= 100000 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)


n, k = map(int, input().split())
# n = 5
# k = 17
print(hideAndSeek(n, k))
