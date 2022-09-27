import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
arr = [list(input()) for _ in range(n)]
# print(arr)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]  # 상하좌우

dic = {'R' : 1, 'G' : 1, 'B' : 0}
visited = [[0]*n for _ in range(n)]
def dfs(x, y):
    visited[x][y] = 1
    color = arr[x][y]
    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == color and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny)

visited2 = [[0]*n for _ in range(n)]
def dfs2(x, y):
    visited2[x][y] = 1
    color = dic[arr[x][y]]
    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        if 0 <= nx < n and 0 <= ny < n and dic[arr[nx][ny]] == color and not visited2[nx][ny]:
            visited2[nx][ny] = 1
            dfs2(nx, ny)

cnt, cnt2 = 0, 0
for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            dfs(r, c)
            cnt += 1
        if not visited2[r][c]:
            dfs2(r, c)
            cnt2 += 1
print(cnt, cnt2)