import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]  # 상하좌우

visited = [[0]*m for _ in range(n)]

q = deque()
for r in range(n):
    for c in range(m):
        if arr[r][c] == 1:
            q.append((r, c))

while q:
    a, b = q.popleft()
    for i in range(4):
        nx = a + dr[i]
        ny = b + dc[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = 1
            arr[nx][ny] = arr[a][b] + 1
            q.append((nx, ny))


def check(array):
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                return -1
            else:
                result = max(result, array[i][j])
    return result-1
print(check(arr))