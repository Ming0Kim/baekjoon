import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    a = input().split()
    x = a[0]
    if len(a) == 1:
        if x == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        y = int(a[1])
        if x == 'add':
            S.add(y)
            # print(S)
            # print()
        elif x == 'remove':
            S.discard(y)
            # print(S)
            # print()

        elif x == 'check':
            if y in S:
                print(1)
                # print(S)
                # print()

            else:
                print(0)
                # print(S)
                # print()

        elif x == 'toggle':
            if y in S:
                S.discard(y)
                # print(S)
                # print()

            else:
                S.add(y)
                # print(S)
                # print()

