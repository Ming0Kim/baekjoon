n = int(input())
arr = [[0]*n for _ in range(n)]
for i in range(n):
    arr[i] = [0] + list(map(int, input().split())) + [0]*(n-i-1)
# print(arr)
for i in range(1, n):
    for j in range(1, len(arr[i])):
        # print(i, j)
        arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
# print(arr)
print(max(arr[n-1]))