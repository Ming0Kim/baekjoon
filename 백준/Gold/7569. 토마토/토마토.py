import sys
input = sys.stdin.readline
from collections import deque

m, n, height = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(height)]

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]  # 상하좌우앞뒤
dh = [0, 0, 0, 0, 1, -1]

q = deque()
for h in range(height):
    for r in range(n):
        for c in range(m):
            if arr[h][r][c] == 1:
                q.append((h, r, c))

while q:
    c, a, b = q.popleft()
    for i in range(6):
        nh = c + dh[i]
        nx = a + dr[i]
        ny = b + dc[i]
        if 0 <= nh < height and 0 <= nx < n and 0 <= ny < m and arr[nh][nx][ny] == 0:
            arr[nh][nx][ny] = arr[c][a][b] + 1
            q.append((nh, nx, ny))


def check(array):
    result = 0
    for k in range(height):
        for i in range(n):
            for j in range(m):
                if array[k][i][j] == 0:
                    return -1
                else:
                    result = max(result, array[k][i][j])
    return result-1
print(check(arr))