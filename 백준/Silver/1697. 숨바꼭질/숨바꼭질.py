from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
second = [0]*100001

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        a = q.popleft()
        if a == k:
            print(second[a])
            break
        for na in (a+1, a-1, 2*a):
            if 0 <= na <= 100000 and not second[na]:
                second[na] = second[a]+1
                q.append(na)
bfs(n)