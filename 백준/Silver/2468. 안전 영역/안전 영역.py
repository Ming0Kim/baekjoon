import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

mx = max(map(max, arr))
mn = min(map(min, arr))

def dfs(x, y, val):
    for j in range(4):
        nx = x + dr[j]
        ny = y + dc[j]
        if 0<= nx <N and 0<= ny <N and not visited[nx][ny] and arr[nx][ny] > val:
            visited[nx][ny] = 1
            dfs(nx, ny, val)


ans = 0
for i in range(mn-1, mx+1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and arr[r][c] > i:
                visited[r][c] = 1
                dfs(r, c, i)
                cnt += 1
                ans = max(ans, cnt)
print(ans)