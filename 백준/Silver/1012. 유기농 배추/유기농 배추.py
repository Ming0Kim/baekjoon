
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 시작 점만 남기고 나머지 1들은 모두 0으로 처리
def dfs(cabbage, r, c):
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if cabbage[ny][nx] == 1:
                cabbage[ny][nx] = 0
                dfs(cabbage, nx, ny)


t = int(input())
for tc in range(1, t+1):
    m, n, k = map(int, input().split())

    # 배추밭
    cabbage = [[0]*m for _ in range(n)]
    # print(cabbage)
    for _ in range(k):
        a, b = map(int, input().split())
        cabbage[b][a] = 1

    # for r in cabbage:
    #     print(*r)

    # 남은 1들만 세면됨
    cnt = 0
    for r in range(m):
        for c in range(n):
            if cabbage[c][r] ==1:
                dfs(cabbage, r, c)
                cnt += 1
    print(cnt)