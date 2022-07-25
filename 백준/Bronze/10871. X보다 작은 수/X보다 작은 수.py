N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
  a = ''
  if i < X:
    a += str(i)+' '
  print(a, end = '')