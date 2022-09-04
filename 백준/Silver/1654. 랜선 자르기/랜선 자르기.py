K, N = map(int, input().split())
klst = [int(input()) for _ in range(K)]
klst.sort()
start = 1
end = klst[-1]
result = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for a in klst:
        cnt += a // mid
    if cnt < N:
        end = mid -1
    else:
        result = mid
        start = mid +1
print(result)