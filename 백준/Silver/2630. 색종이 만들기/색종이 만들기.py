# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

color = [0]*2
def dfs(x, y, n):
    check = arr[x][y]
    for r in range(x, x+n):
        for c in range(y, y+n):
            if arr[r][c] != check:
                for i in range(2):
                    for j in range(2):
                        dfs(x+i*n//2, y+j*n//2, n//2)
                return
    color[check] += 1

dfs(0, 0, N)
for i in color:
    print(i)