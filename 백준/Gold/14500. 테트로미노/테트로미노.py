import sys
input = sys.stdin.readline

tet = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    [(0, 0), (0, 1), (1, 0), (1, 1)],

    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (0, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],

    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 1), (0, 0), (1, 2), (0, 2)],

    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(0, 1), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],

    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 1), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)]
]

# tet 맞는지 확인하는 코드
# for a in tet:
#     arr = [[0]*5 for _ in range(5)]
#     for i in a:
#         arr[i[0]][i[1]] = 1
#
#     for b in arr:
#         print(*b)
#     print()

# 리스트 안의 값들이 범위를 벗어나지 않는지 체크
def check(lst):
    for a in lst:
        if 0 <= r+a[0] < N and 0 <= c+ a[1] <M:
            pass
        else:
            return 0
    else:
        return 1

# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 각각의 shape에 대한 최댓값을 저장할 리스트
# shape = [0]*19
shape = 0
for r in range(N):
    for c in range(M):
        for i in tet:
            if check(i) == 0:
                pass
            else:
                sh = 0
                for k in i:
                    sh += arr[r+k[0]][c+k[1]]
                if sh > shape:
                    shape = sh

print(shape)

