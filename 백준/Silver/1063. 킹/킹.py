# A : 65 B : 66 ...

# 딕셔너리 이용
move = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
        'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}

# 입력
k, d, n = input().split()
rk = int(k[1])
ck = ord(k[0]) - 64
rd = int(d[1])
cd = ord(d[0]) - 64

# 주어진 움직임에 대하여
for _ in range(int(n)):
    m = input()
    r, c = move[m][0], move[m][1]
    # 킹이 범위안에 있다면
    if 1 <= rk + r <= 8 and 1 <= ck + c <= 8:
        # 돌과 겹친다면
        if rk + r == rd and ck + c == cd:
            # 돌이 범위 안에 있다면,
            if 1 <= rd + r <= 8 and 1 <= cd + c <= 8:
                rd += r
                cd += c
                rk += r
                ck += c
            else:
                pass
        else:
            rk += r
            ck += c
    else:
        pass

# 출력
print(f'{chr(ck+64)}{rk}')
print(f'{chr(cd+64)}{rd}')
