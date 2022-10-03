n, m = map(int, input().split())
a, b = n, m
c, d = 1, 1
while True:
    c *= a
    a -= 1
    if a == n-m:
        break
while True:
    d *= b
    b -= 1
    if b == 0:
        break
print(c//d)