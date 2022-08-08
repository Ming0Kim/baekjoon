dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
string = input()

num = 0
for i in string:
    for j in dial:
        if i in j:
            num += dial.index(j)+3
print(num)
