n = int(input())
lst = []
for _ in range(n):
    lst.append(tuple(map(int, input().split())))
lst.sort(key = lambda x : (x[0], x[1]))
for i in lst:
    print(*i)