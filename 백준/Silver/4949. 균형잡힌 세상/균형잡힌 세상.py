import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    a = input()
    if a == '.':
        break
    stk = []
    result = 'yes'
    ans = []
    for w in a:
        if w == '(':
            stk.append('(')
        elif w == '[':
            stk.append('[')
        elif w == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                result = 'no'
                break
        elif w == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                result = 'no'
                break
    if stk:
        result = 'no'
    print(result)