import sys
input = sys.stdin.readline

# 입력
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 자신보다 키, 몸무게 둘 다 큰 사람 수 + 1 출력
for i in range(n):
    sm = 1
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            sm += 1
    print(sm, end=' ')