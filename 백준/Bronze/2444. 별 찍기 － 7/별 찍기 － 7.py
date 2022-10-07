n = int(input())
for i in range(1, 2*n):
    if i > n:
        i = n-(i-n)
    print(' '*(n-i) + '*'*(2*i-1))