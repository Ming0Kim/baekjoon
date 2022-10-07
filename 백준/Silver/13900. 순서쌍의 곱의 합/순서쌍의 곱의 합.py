import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
sm = sum(lst)
result = 0
for i in lst:
    sm -= i
    result += i*sm
print(result)