N = int(input())

if N%5 == 0:
    print(N//5)
else:
    k = 0
    while N > 0:
        N -= 3
        k += 1
        if N % 5 == 0:
            k += N//5
            print(k)
            break
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N == 0:
            print(p)
            break