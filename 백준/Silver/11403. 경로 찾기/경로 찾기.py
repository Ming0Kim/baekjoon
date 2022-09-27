n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(i)

visited = [0]*n
for r in range(n):
    dfs(r)
    for c in range(n):
        if visited[c] == 1:
            print('1', end=' ')
        else:
            print('0', end=' ')
    visited = [0]*n
    print()