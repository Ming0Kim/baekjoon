import sys
input = sys.stdin.readline
# 입력 : apple
N = int(input())
K = int(input())
apple = []
for _ in range(K):
    a, b = map(int, input().split())
    apple.append((a, b))
# print(apple)
# 2차원 arr 생성 후 apple 위치 등록
arr = [[0] * (N+1) for _ in range(N+1)]
for (a, b) in apple:
    arr[a][b] = 2
# print(arr)
# 입력 : 방향 변환
L = int(input())
sec = []
for _ in range(L):
    x, c = input().split()
    sec.append((int(x), c))
# print(sec)
# 방향 정보 / 우 : +1 / 좌 : -1
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# 뱀 길이 위치 정보
snake = [[1, 1]]
d = t = 0  # d : 방향 t : 초
while True:
    t +=1
    for sn in snake:
        dr = snake[-1][0] + dir[d][0]
        dc = snake[-1][1] + dir[d][1]
    # 범위를 벗어나거나, 뱀이 물릴경우
    if dr < 1 or dr > N or dc <1 or dc > N or [dr, dc] in snake:
        print(t)
        break
    else:
        snake.append([dr,dc])
        # print(snake)
        # 사과 만남
        if arr[dr][dc] == 2:
            arr[dr][dc] = 0
            # print(snake)
            pass
        else:
            snake.pop(0)
            # print(snake)
    # 방향 변환
    for s in sec:
        if t == s[0]:
            if s[1] == 'D':  # 오른쪽 전환
                d += 1
                d = d%4
            if s[1] == 'L':  # 왼쪽으로 전환
                d -= 1
                d = d%4

