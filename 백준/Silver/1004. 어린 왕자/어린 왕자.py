import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0

    # 원 각각의 영역을 circle에 튜플로 append
    for a in range(n):
        cx, cy, r = map(int, input().split())

        # 두 점의 거리
        dis1 = (x1-cx)**2 + (y1-cy)**2
        dis2 = (x2-cx)**2 + (y2-cy)**2

        # 두 점이 같은 원 안에 있음
        if dis1 < r**2 and dis2 < r**2:
            pass
        # 한 점이 원 내부에 있을 때
        elif dis1 < r**2:
            cnt += 1
        elif dis2 < r**2:
            cnt += 1

    print(cnt)