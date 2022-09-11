import sys
input = sys.stdin.readline
q = []
N = int(input())
for _ in range(N):
    order = input().split()
    # print(order)
    # push
    if order[0] == 'push':
        q.append(order[1])
    # pop
    elif order[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    # size
    elif order[0] == 'size':
        print(len(q))
    # empty
    elif order[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    # front
    elif order[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    # back
    elif order[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)