import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * 10001
for _ in range(N):
    a = int(input())
    lst[a] += 1
for j in range(10001):
    if lst[j] != 0:
        for k in range(lst[j]):
            print(j)