S = set(list(range(1, 31, 1)))
for _ in range(28):
    n = int(input())
    S.remove(n)
for i in S:
    print(i)