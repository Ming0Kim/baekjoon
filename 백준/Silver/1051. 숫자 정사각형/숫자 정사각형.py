
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

mx = 0
for i in range(n-1, 0, -1):
    for r in range(n):
        for c in range(m):
            if 0<=r+i<n and 0<=c+i<m and arr[r][c] == arr[r+i][c] == arr[r][c+i] == arr[r+i][c+i]:
                a = (i+1)**2
                mx = max(mx, a)

print(mx if mx else 1)
