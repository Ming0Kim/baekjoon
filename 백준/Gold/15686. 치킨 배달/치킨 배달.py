from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            house.append([r,c])
        if arr[r][c] == 2:
            chicken.append([r,c])
# print(chicken)
# print(house)
chickenstore = list(combinations(chicken, M))
# print(chickenstore)

chickmeter = []
for i in chickenstore:
    sm = 0
    for j in house:
        housemn = 10000000
        for k in range(M):
            tmp = abs(i[k][0] - j[0]) + abs(i[k][1] - j[1])
            if tmp < housemn:
                housemn = tmp
        # print(housemn)
        sm += housemn
    chickmeter.append(sm)
print(min(chickmeter))

# a = [([0, 1], [3, 0]), ([0, 1], [4, 0]), ([0, 1], [4, 1]), ([0, 1], [4, 4]), ([3, 0], [4, 0]), ([3, 0], [4, 1]), ([3, 0], [4, 4]), ([4, 0], [4, 1]), ([4, 0], [4, 4]), ([4, 1], [4, 4])]
# for i in a:
#     print(i[0][0])