new = []
for _ in range(10):
  a = int(input())
  rest = a%42
  if rest not in new:
    new.append(rest)
print(len(new))