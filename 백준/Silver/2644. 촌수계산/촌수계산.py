def dfs(n):
    visited[n] = 1
    for i in arr[n]:
        if not visited[i]:
            result[i] = result[n] +1
            dfs(i)

# 초기화
N = int(input())
p1, p2 = map(int, input().split())
M = int(input())
arr = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
result = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(p1)
print(result[p2] if result[p2] >0 else -1)