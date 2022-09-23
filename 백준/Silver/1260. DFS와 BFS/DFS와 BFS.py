from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(n):
    print(n, end=' ')
    visited[n] = 1
    for i in arr[n]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

def bfs(b):
    q = deque([b])
    visited[b] = 1
    while q:
        a = q.popleft()
        print(a, end=' ')
        for i in arr[a]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())
arr = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)

for i in arr:
    i.sort()

visited = [0]*(N+1)
dfs(V)
print()
visited = [0]*(N+1)
bfs(V)
