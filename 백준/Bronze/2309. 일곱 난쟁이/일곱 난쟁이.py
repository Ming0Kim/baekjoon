lst = []
for _ in range(9):
    lst.append(int(input()))
# print(lst)
sm = sum(lst)
flag = 0
for i in range(8):
    for j in range(i+1, 9):
        # print(i, j)
        if sm - lst[i] - lst[j] == 100:
            flag = 1
            lst.pop(j)
            lst.pop(i)
            break
    if flag:
        break

lst.sort()
for j in lst:
    print(j)