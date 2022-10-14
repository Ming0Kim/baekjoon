T = int(input())
for _ in range(T):
    lst = []
    for i in range(4):
        a, b = map(int, input().split())
        lst.append((a, b))
    lst.sort()
    # print(lst)
    ans = 0
    if ((lst[0][0] - lst[1][0])**2 + (lst[0][1] - lst[1][1])**2) == ((lst[2][0] - lst[3][0])**2 + (lst[2][1] - lst[3][1])**2) == ((lst[0][0] - lst[2][0])**2 + (lst[0][1] - lst[2][1])**2) == ((lst[1][0] - lst[3][0])**2 + (lst[1][1] - lst[3][1])**2):
        if ((lst[0][0] - lst[3][0])**2 + (lst[0][1] - lst[3][1])**2) == ((lst[2][0] - lst[1][0])**2 + (lst[2][1] - lst[1][1])**2):
            if ((lst[0][0] + lst[3][0])/2 , (lst[0][1] + lst[3][1])/2) == ((lst[1][0] + lst[2][0])/2 , (lst[1][1] + lst[2][1])/2):
                ans = 1
    print(ans)