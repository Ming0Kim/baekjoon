T = int(input())
for _ in range(T):
    R, S = input().split()
    for i in S:
        P = i*int(R)
        print(P,end='')
    print(end=' ')