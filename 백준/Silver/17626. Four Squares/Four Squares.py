n = int(input())

dp = [0]*50001
dp[1] = 1

for i in range(1, n+1):
    ans = 0
    x = i
    while x:
        a = int(x**0.5) **2
        x -= a
        ans += 1
    dp[i] = ans

    for j in range(1, int(i**0.5) +1):
        dp[i] = min(dp[i], dp[j*j] + dp[i - j*j])

print(dp[n])