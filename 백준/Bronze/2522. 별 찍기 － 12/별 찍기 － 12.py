n = int(input())
for i in range(1, 2*n):
    if i > n:
        i = -i + 2*n
    print(' '*(n-i) + '*'*i)