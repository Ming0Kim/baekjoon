# 입력
A, B, C = map(int,input().split())

if B-C == 0:
    print(-1)
elif A/(C-B)+1 <0:
    print(-1)
else:
    print(int(A/(C-B))+1)