from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    lst = deque(list(map(int, input().split())))
    cnt = 0

    while lst:
        best = max(lst)
        front = lst.popleft()
        m -= 1

        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            lst.append(front)
            if m < 0:
                m += len(lst)