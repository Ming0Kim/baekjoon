# 입력
N, r, c = map(int, input().split())

sm = 0
# 4사분면으로 나누어서
while N!=0:
    if r < 2**(N-1):
        if c < 2**(N-1):      # 2사분면
            k = 0
            sm += k*4**(N-1)

        else:                 # 1사분면
            k = 1
            sm += k*4**(N-1)
            c -= 2**(N-1)  # 다음 차례에는 다시 사분면을 나눌 수 있게

    else:
        if c < 2 ** (N - 1):  # 3사분면
            k = 2
            sm += k * 4 ** (N - 1)
            r -= 2**(N-1)

        else:                 # 4사분면
            k = 3
            sm += k * 4 ** (N - 1)
            r -= 2**(N-1)
            c -= 2**(N-1)
    N -= 1
print(sm)