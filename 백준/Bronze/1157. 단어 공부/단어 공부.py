string = input()
string = string.lower()

sstr = sorted(set(list(string)))
cnt = []

for str in sstr:
    cnt.append(string.count(str))

if len(sstr) == 1 :
    print(sstr[cnt.index(max(cnt))].upper())

elif sorted(cnt,reverse=True)[0] == sorted(cnt,reverse=True)[1]:
    print('?')

else:
    print(sstr[cnt.index(max(cnt))].upper())