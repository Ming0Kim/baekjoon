dictionary = {
    1: 1,
    2: 2
}

def rec(n):
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = rec(n-1) + rec(n-2)
        return dictionary[n]

n = int(input())
print(rec(n)%10007)