T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N%H == 0 :
        floor = str(H)
        room = N//H
    else:
        floor = str(N%H)
        room = N // H + 1

    if room//10 == 0:     # 한 자리라면,
        room = '0' + str(room)
    room = str(room)
    print(floor+room)