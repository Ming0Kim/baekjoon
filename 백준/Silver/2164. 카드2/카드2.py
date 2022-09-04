# 데크 라이브러리 처음 써봤당 
from collections import deque
N = int(input())
lst = deque([i for i in range(1, N+1)])

while len(lst) > 1:
    lst.popleft()
    lst.append(lst.popleft())
print(*lst)