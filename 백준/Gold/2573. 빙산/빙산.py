import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]  # 상하좌우

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
year = 0
while True:
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] and not visited[r][c]:
                dfs(r, c)
                cnt += 1

    memory = [[0]*m for _ in range(n)]
    flag = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c]:
                flag = 1
                water = 0
                for i in range(4):
                    if 0 <= r+dr[i] < n and 0 <= c+dc[i] < m and arr[r+dr[i]][c+dc[i]] == 0:
                        water += 1
                if arr[r][c] - water < 0:
                    memory[r][c] = 0
                else:
                    memory[r][c] = arr[r][c] - water
    # for i in memory:
    #     print(*i)

    # 빙산이 없으면
    if flag == 0:
        print(0)
        break

    if cnt > 1:
        print(year)
        break
    else:
        year += 1

    arr = memory
    memory = [[0]*m for _ in range(n)]