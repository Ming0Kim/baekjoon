n = int(input())

def fac(N):
    if N > 1:
        return N * fac(N-1)
    else:
        return 1
a = fac(n)
a = str(a)
a = a[::-1]
cnt = 0
for i in range(len(a)):
    if a[i] == '0':
        cnt +=1
    else:
        print(cnt)
        break
