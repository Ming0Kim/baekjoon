from collections import deque

a, b = map(int, input().split())

def bfs(n):
    q = deque()
    q.append([n, 1])
    while q:
        a = q.popleft()
        if a[0] == b:
            print(a[1])
            return
        for i in (a[0]*2, 10*a[0]+1):
            if i <= b:
                q.append([i, a[1]+1])
    print(-1)

bfs(a)