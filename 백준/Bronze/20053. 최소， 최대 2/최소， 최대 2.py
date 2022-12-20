T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'{min(lst)} {max(lst)}')