import sys
input = sys.stdin.readline
sys.setrecursionlimit(50**2)
def dfs(x, y):
    visited[x][y] = 1
    for i in range(8):
        if 0 <= x+dr[i] < h and 0 <= y+dc[i] < w and arr[x+dr[i]][y+dc[i]] == 1 and not visited[x+dr[i]][y+dc[i]]:
            visited[x+dr[i]][y+dc[i]] = 1
            dfs(x+dr[i], y+dc[i])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]   # 8 1 2
dc = [0, 1, 1, 1, 0, -1, -1, -1]   # 7   3
                                   # 6 5 4
# 입력
while True:
    a = list(map(int, input().split()))
    if a == [0, 0]:
        break
    w, h = a
    arr = [list(map(int, input().split())) for i in range(h)]
    # print(w, h, arr)

    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for r in range(h):
        for c in range(w):
            if arr[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                cnt += 1
    print(cnt)