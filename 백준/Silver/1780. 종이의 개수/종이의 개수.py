# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

paper = [0]*3

def dfs(x, y, n):
    check = arr[x][y]
    for r in range(x, x+n):
        for c in range(y, y+n):
            if arr[r][c] != check:
                for i in range(3):
                    for j in range(3):
                        dfs(x+n//3*i, y+n//3*j, n//3)
                return
    paper[check] += 1

dfs(0, 0, N)

for i in range(-1, 2):
    print(paper[i])