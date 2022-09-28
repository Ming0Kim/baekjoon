import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
# print(lst)
mx = -100*n
val = sum(lst[0:k])
result = []
result.append(val)
for i in range(k, n):
    val = val + lst[i] - lst[i-k]
    result.append(val)
print(max(result))