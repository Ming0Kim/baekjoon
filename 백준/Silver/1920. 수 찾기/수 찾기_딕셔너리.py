# 입력
N = int(input())
NA = input().split()
# 딕셔너리 이용한 try except 구문
dic = {}
for a in NA:
    dic[a] = 1

M = int(input())
NB = input().split()
# try except는 안 좋은 거라 한 거 같은데...
for b in NB:
    try:
        print(dic[b])
    except KeyError:
        print(0)