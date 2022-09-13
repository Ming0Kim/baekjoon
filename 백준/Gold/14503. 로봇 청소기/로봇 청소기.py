def four(r, c):
    for i in range(4):
        if 0 > r+dir[i][0] or r+dir[i][0]>= N or 0 > c+dir[i][1] or c+dir[i][1] >= M:
            continue
        elif arr[r+dir[i][0]][c+dir[i][1]] == 0:
            return 1
        else:
            pass
    return 0

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]         # 북 동 남 서
dleft = [(0, -1), (-1, 0), (0, 1), (1, 0)]       # 서 북 동 남
arr[r][c] = 2
clean = 1
while True:
    if not four(r ,c):
        if 0 > r-dir[d][0] or r-dir[d][0] >= N or 0 > c-dir[d][1] or c-dir[d][1] >= M:
            print(clean)
            break
        r -= dir[d][0]
        c -= dir[d][1]
        if 0 <= r < N and 0 <= c < M:
            if arr[r][c] == 1:
                print(clean)
                break


    elif 0<= r+dleft[d][0] <N and 0 <= c+dleft[d][1] < M and arr[r+dleft[d][0]][c+dleft[d][1]] == 0:
        d -= 1
        d = d%4
        r += dir[d][0]
        c += dir[d][1]
        arr[r][c] = 2
        clean += 1
    else:
        d -= 1
        d = d%4