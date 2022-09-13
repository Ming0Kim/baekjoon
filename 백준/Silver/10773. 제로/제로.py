K = int(input())
stk = []
num = 0
for _ in range(K):
    a = int(input())
    num += a
    if a == 0:
        num -= stk.pop()
    else:
        stk.append(a)
print(num)