from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dr[i]
            ny = b + dc[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                arr[nx][ny] = arr[a][b] + 1
                q.append((nx, ny))

bfs(0, 0)
print(arr[n-1][m-1])