word = input()
lst = []
length = len(word)
for i in range(1, length-1):
    for j in range(i, length):
        if word[i:j]:
            lst.append(word[:i][::-1]+word[i:j][::-1]+word[j:][::-1])
lst.sort()
print(lst[0])