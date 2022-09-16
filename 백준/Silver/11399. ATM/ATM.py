N = int(input())
P = list(map(int, input().split()))
for i in range(N):
    for j in range(i+1, N):
        if P[i] > P[j] :
            P[i], P[j] = P[j], P[i]
sm = 0
for i in range(N):
    sm += P[i]*(N-i)
print(sm)