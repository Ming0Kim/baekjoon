x, y, w, h = map(int, input().split())
a = w-x
b = h-y
lst = [a, b, x, y]
print(min(lst))