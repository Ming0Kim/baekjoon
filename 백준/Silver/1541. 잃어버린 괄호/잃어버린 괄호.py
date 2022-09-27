
word = input()
num = word.split('-')
result = []
for i in num:
    sm = 0
    s = i.split('+')
    for a in s:
        sm += int(a)
    result.append(sm)

ans = result[0]
for a in range(1, len(result)):
    ans -= result[a]
print(ans)