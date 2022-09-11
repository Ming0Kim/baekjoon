N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a,b))
lam = sorted(lst, key = lambda x : (x[1], x[0]))
for (a, b) in lam:
    print(a, b)