memo = [0]*41
memo[0] = [1, 0]
memo[1] = [0, 1]
def fib(n):
    if memo[n] == 0:
        memo[n] = [fib(n-1)[0] + fib(n-2)[0], fib(n-1)[1] + fib(n-2)[1]]
    return memo[n]

t = int(input())
for _ in range(t):
    N = int(input())
    print(*fib(N))