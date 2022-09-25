import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

def bfs(arr, start):
    people = [0]*(n+1)
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        a = q.popleft()
        for i in arr[a]:
            if not visited[i]:
                people[i] = people[a] + 1
                q.append(i)
                visited[i] = 1
    return sum(people)

result = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    result.append(bfs(lst, i))
print(result.index(min(result))+1)