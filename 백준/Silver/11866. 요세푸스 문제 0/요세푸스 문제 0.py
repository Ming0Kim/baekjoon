N, K = map(int, input().split())
stk = [0]
for i in range(1, N+1):
    stk.append(i)
result = []
j = 1
while len(result) != N:
    if j%K == 0:
        result.append(stk[j])
        stk[j] = 0
    else:
        stk.append(stk[j])
        stk[j] = 0
    j += 1
print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[N-1], end='')
print('>')


