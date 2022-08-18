import sys
input = sys.stdin.readline

import math

# 입력
t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # (x1, y1) 과 (x2, y2) 사이의 거리
    bet = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # 두 점의 위치가 같고 각각 거리가 같지 않은 경우 : 0
    if (x1, y1) == (x2, y2) and r1 != r2:
        print(0)

    # 두 점이 위치가 같고 각각의 거리가 같은 경우 : -1(무한대)
    elif (x1, y1) == (x2, y2) and r1 == r2:
        print(-1)

    # 두 점 사이의 거리가 각각 거리의 합보다 크다면 가능한 위치 개수 : 2
    elif abs(r1-r2) < bet < r1 + r2:
        print(2)

    # 두 점 사이의 거리가 각각 거리의 합과 같다면 가능한 위치 개수 : 1
    elif abs(r1-r2) == bet or bet == r1 + r2:
        print(1)

    else:
        print(0)