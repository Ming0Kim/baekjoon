# import sys
# input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    site, pw = input().split()
    dic[site] = pw
# print(dic)
for i in range(M):
    a = input()
    print(dic[a])