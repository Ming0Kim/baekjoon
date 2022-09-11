import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)
# 이분탐색 이용
while start <= end:
    mid = (start + end)//2
    cut = 0
    for i in tree:
        if i - mid > 0:
            cut += i - mid
    # print(cut)
    if cut < M:
        end = mid -1
    else:
        start = mid +1
print(end)