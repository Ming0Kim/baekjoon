arr = [[0] * 15 for _ in range(15)]
lst = [0]*15
for a in range(1, 15):
    lst[a] = a
arr[0] = lst
for i in range(1, 15):
    for j in range(1, 15):
        for k in range(1, j+1):
            arr[i][j] += arr[i-1][k]
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n])