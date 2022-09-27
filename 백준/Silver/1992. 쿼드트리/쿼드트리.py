def quad(x, y, n):
    global tree
    val = arr[x][y]
    for r in range(x, x+n):
        for c in range(y, y+n):
            if arr[r][c] != val:
                print('(', end='')
                quad(x, y, n//2)
                quad(x, y+n//2, n//2)
                quad(x+n//2, y, n//2)
                quad(x+n//2, y+n//2, n//2)
                print(')', end='')
                return

    if val == 0:
        print('0', end='')
        return
    else:
        print('1', end='')
        return


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
# print(arr)
tree = ''
quad(0, 0, n)
print(tree)