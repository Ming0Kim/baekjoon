import sys
input = sys.stdin.readline
def bin(cards, ms, start, end):
    if start > end:
        return 0
    mid = (start + end)//2
    if cards[mid] == ms:
        return cnt.get(ms)
    elif cards[mid] < ms:
        return bin(cards, ms, mid +1 , end)
    else:
        return bin(cards, ms, start, mid-1)

N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
lst = list(map(int, input().split()))

cnt = {}
for i in card:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in lst:
    print(bin(card, i, 0, N-1), end=' ')