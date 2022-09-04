import copy
# 입력
N = int(input())
lst = [int(input()) for _ in range(N)]
relst = copy.deepcopy(lst)
# 검증용 갯수
stk = []
result = []
plmn = []
for i in range(1, N+1):
    while stk and stk[-1] == lst[0]:
        plmn.append('-')
        stk.pop()
        result.append(lst.pop(0))
    stk.append(i)
    plmn.append('+')
while stk and stk[-1] == lst[0]:
    plmn.append('-')
    stk.pop()
    result.append(lst.pop(0))
if relst != result or stk:
    print("NO")
else:
    for a in plmn:
        print(a)


