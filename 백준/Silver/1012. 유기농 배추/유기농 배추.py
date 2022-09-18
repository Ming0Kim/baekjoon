import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

dr = [-1, 0, 1, 0]  # 상 좌 하 우
dc = [0, -1, 0, 1]

def dfs(lst, r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
            arr[nr][nc] = 0
            dfs(lst, nr, nc)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for i in range(n)]
    for K in range(k):
       x, y = map(int, input().split())
       arr[y][x] = 1
    cnt = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                dfs(arr, r, c)
                cnt += 1
    print(cnt)