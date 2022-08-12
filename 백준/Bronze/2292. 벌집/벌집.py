# 1 7 19 37 61 ...

'''
1 -> 7 // 6
7 -> 19 // 12
19 -> 37 // 18
37 -> 61 // 24

a`n+1 - a`n = 6n
a2 - a1 = 6
a3 - a2 = 12
...
a`n - a`n-1 = 6(n-1)

an = 3(n-1)*n + 1
'''
import math

# 입력
N = int(input())

# 근의 공식 이용
k = (3+(9-12*(1-N))**0.5)/6
print(math.ceil(k))