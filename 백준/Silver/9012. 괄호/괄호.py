t = int(input())
for tc in range(t):
    bracket = input()
    stk = []
    ans = 'YES'
    for i in range(len(bracket)):
        if bracket[i] == ')':
            if len(stk) == 0:
                ans = 'NO'
            elif stk[-1] == '(':
                stk.pop()
        else:
            stk.append(bracket[i])
    if stk:
        ans = 'NO'
    print(ans)