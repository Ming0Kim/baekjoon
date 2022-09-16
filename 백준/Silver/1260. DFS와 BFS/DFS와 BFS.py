from collections import deque

def dfs(start):
    print(start, end=' ')
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)
            visited[i] = 1

def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in arr[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

visited = [0]*(n+1)
dfs(v)
print()
visited = [0]*(n+1)
bfs(v)