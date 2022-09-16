import sys
input = sys.stdin.readline
from collections import deque
n, target = map(int, input().split())
coin = deque()
# print(coin)
for _ in range(n):
    coin.appendleft(int(input()))
# print(coin)
cnt = 0

for i in coin:
    # print(i)
    if target - i < 0:     # 타겟과 동전의 차가 0보다 작으면,
        pass
    else:
        while True: # 타겟이 0보다 크거나 같을 때까지
            if target < i:
                break
            target -= i    # 타겟에서 동전을 뺀다
            cnt += 1       # 카운트 + 1 해준다
    # print(i, cnt, target)
    if target == 0:        # 타겟이 0이면, for 문을 끝낸다
        break
print(cnt)