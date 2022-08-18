import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = [0]
sm = 0
for i in lst:
    sm += i
    lst2.append(sm)

for _ in range(m):
    i, j = map(int, input().split())
    print(lst2[j] - lst2[i-1])