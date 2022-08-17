lst = [1, 1, 1]
for i in range(3, 101):
    lst.append(lst[i-3] + lst[i-2])

t = int(input())
for _ in range(t):
    print(lst[int(input())-1])