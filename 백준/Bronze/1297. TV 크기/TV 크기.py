D, H, W = map(int, input().split())
x = (D**2/(W**2/H**2+1))**0.5
y = W/H*x
print(f'{int(x)} {int(y)}')
