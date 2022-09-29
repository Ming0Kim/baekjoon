def ncr(n, r, s):
    if r == 0:
        print(*sorted(comb))
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            ncr(n, r-1, i+1)

n, m = map(int, input().split())

A = [i for i in range(1, n+1)]
comb = [0]*m
ncr(n, m, 0)