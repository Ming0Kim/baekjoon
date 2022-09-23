c = int(input())
net = int(input())
network = [[] for _ in range(c+1)]
for _ in range(net):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
# print(network)
cnt = 0
visited = [0]*(c+1)
def dfs(n):
    global cnt
    visited[n] = 1
    for a in network[n]:
        if not visited[a]:
            visited[a] = 1
            cnt += 1
            dfs(a)
dfs(1)
# print(visited)
print(cnt)