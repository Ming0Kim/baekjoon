# ord('a') = 97

L = int(input())
word = input()
sm = 0
for i in range(L):
    ai = ord(word[i])-96
    sm += ai*31**i
print(sm%1234567891)