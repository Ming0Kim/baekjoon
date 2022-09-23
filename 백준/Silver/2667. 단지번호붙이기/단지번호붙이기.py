def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=N:
        return 0
    if arr[x][y] == 1:
        global cnt
        cnt += 1
        arr[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return 1
    return 0


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)

dx = [1, -1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

cnt = 0
color = []

for i in range(N):
    for j in range(N):
        if dfs(i, j) == 1:
            color.append(cnt)
            cnt = 0
print(len(color))
color.sort()
for i in color:
    print(i)