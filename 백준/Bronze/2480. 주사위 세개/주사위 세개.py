a, b, c = map(int,input().split())
list_a = [a, b, c]
if a==b==c:
  print(10000 + 1000*a)
elif a==b:
  print(1000 + 100*a)
elif b ==c :
  print(1000 + 100*b)
elif c==a:
  print(1000 + 100*c)
else:
  print(sorted(list_a)[-1]*100)