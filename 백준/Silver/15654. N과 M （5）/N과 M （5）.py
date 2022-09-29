n, m = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst.sort()
s = []

def dfs():
    if len(s)==m:
        print(*s)
        return
    for i in lst:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()