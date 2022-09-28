from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    a = input().split()
    # print(a)
    # push
    if len(a) > 1:
        q.append(int(a[1]))
    # pop
    elif a[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    # size
    elif a[0] == 'size':
        print(len(q))
    # empty
    elif a[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    # front
    elif a[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    # back
    elif a[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)