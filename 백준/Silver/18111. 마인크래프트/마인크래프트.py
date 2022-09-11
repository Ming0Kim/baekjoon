# 입력
N, M, B = map(int, input().split())
arr = [[]*M for _ in range(N)]

mn = 500
mx = 0
for i in range(N):
    arr[i] = list(map(int, input().split()))
    tmp1 = max(arr[i])
    tmp2 = min(arr[i])
    if tmp1 > mx:
        mx = tmp1
    if tmp2 < mn:
        mn = tmp2

result = []
for j in range(mn, mx+1):
    b = B
    time = 0
    for r in range(N):
        for c in range(M):
            tmp = arr[r][c]
            if tmp > j:
                b += tmp-j
                time += 2*(tmp-j)
            else:
                b -= j-tmp
                time += j-tmp
    if b >= 0:
        result.append((time, j))

a = sorted(result, key=lambda x: (x[0],-x[1]))[0]
print(*a)
