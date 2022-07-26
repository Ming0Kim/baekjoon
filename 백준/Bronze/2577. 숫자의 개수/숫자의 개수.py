A = int(input())
B = int(input())
C = int(input())

d = A*B*C
string = str(d)

for i in range(10):
  print(string.count(str(i)))