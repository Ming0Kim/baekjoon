N = int(input())
lst = list(map(int, input().split()))
sortlst = sorted(list(set(lst)))
dic = {sortlst[i] : i for i in range(len(sortlst))}

for i in lst:
    print(dic[i], end=' ')