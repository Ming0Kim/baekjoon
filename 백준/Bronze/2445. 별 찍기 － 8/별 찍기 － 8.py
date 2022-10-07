n = int(input())
for i in range(1, 2*n):
    if i > n:
        i = n-(i-n)
    print('*'*i + ' '*2*(n-i) + '*'*i)