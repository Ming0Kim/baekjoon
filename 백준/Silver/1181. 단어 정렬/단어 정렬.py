n = int(input())
word = []
for _ in range(n):
    a = input()
    word.append(a)
word = list(set(word))
word = sorted(word)
word = sorted(word, key=len)

for i in word:
    print(i)