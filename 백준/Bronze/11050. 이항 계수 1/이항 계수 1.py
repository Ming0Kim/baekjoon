N, K = map(int, input().split())
nk = N - K

def fac(n):
    if n > 1:
        return n*fac(n-1)
    else:
        return 1
print(fac(N)//(fac(K)*fac(nk)))