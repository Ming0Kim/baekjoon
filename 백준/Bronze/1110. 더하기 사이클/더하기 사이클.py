N = int(input())
new = N
cnt = 0

while True:
  a = new//10
  b = new%10
  c = a+b
  d = b*10 + c%10
  new = d
  cnt += 1
  if new == N:
    break
print(cnt)