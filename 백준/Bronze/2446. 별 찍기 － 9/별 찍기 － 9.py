n = int(input())
for i in range(0, 2*n-1):
    if i >= n:
        i = n-(i-n)-2
    print(' '*i + '*'*(2*(n-i)-1))