'''
# 테스트케이스 추가
1
6
hat headgear
sunglasses eyewear
turban headgear
mask face
sunglasses face
makeup face
# 출력 : 23
'''

import sys
input = sys.stdin.readline

# 입력
t = int(input())
for _ in range(t):
    dic = {}
    n = int(input())

    for i in range(n):
        a, b = input().split()
        if b in dic:
            dic[b].append(a)
        else:
            dic[b] = [a]
    # print(dic)

    cnt = 1
    for a in dic:
        cnt *= len(dic[a]) +1
    print(cnt-1)