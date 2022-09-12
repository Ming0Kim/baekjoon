import sys
input = sys.stdin.readline

N = input()
n = int(N)
for i in range(1, n):
    sm = i
    for j in range(len(str(i))):
        sm += int(str(i)[j])
    if sm == n:
        print(i)
        break
else:
    print(0)