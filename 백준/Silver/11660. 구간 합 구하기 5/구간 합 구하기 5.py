import sys
input = sys.stdin.readline
# 초기화
n, m = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    arr[i] = [0] + list(map(int, input().split()))
# 행 별 합 구하기
for r in range(n+1):
    for c in range(1, n+1):
        arr[r][c] += arr[r][c-1]
# 열 별 합 구하기
for r in range(n+1):
    for c in range(1, n+1):
        arr[c][r] += arr[c-1][r]
# for i in arr:
#     print(*i)
# 좌표 초기화
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])