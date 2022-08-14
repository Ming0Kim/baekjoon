# 입력
N = int(input())

sm = 0
lst = list(map(int, input().split()))

def pri(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

sm = 0
for i in lst:
    a = pri(i)
    sm += a
print(sm)
