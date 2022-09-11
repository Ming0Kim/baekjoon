import sys
input = sys.stdin.readline
stk = []
N = int(input())
for _ in range(N):
    order = input().split()
    # print(order)
    # push
    if order[0] == 'push':
        stk.append(int(order[1]))
    # pop
    elif order[0] == 'pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)
    # size
    elif order[0] == 'size':
        print(len(stk))
    # empty
    elif order[0] == 'empty':
        if stk:
            print(0)
        else:
            print(1)
    # top
    elif order[0] == 'top':
        if stk:
            print(stk[-1])
        else:
            print(-1)