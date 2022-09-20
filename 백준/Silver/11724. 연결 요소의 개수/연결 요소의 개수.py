import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(v):
    visited[v] = 1
    for i in arr[v]:
        if visited[i] == 0:
            dfs(i)
cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)
# print(visited)

print(cnt)