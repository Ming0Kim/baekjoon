def preorder(n):    # 전위순회
    if n:
        print(chr(n+64), end='')    # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):     # 중위순회
    if n:
        inorder(ch1[n])
        print(chr(n+64), end='')    # visit(n)
        inorder(ch2[n])

def postorder(n):   # 후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(chr(n+64), end='')    # visit(n)

V = int(input())
# print(ord('A')) # 65
ch1 = [0] * (V+1)
ch2 = [0] * (V + 1)
for _ in range(V):
    lst = input().split()
    if lst[1] != '.':
        ch1[ord(lst[0])-64] = ord(lst[1])-64
    if lst[2] != '.':
        ch2[ord(lst[0])-64] = ord(lst[2])-64
    # print(lst, ch1, ch2)
root = 1
preorder(root)
print()
inorder(root)
print()
postorder(root)