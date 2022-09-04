# 이진탐색 함수
def bin(LST, B, START, END):
    while START <= END:
        mid = (START + END)//2
        if LST[mid] == B:
            return mid
        elif LST[mid] > B:
            END = mid -1
        else:
            START = mid +1
    return None

N = int(input())
NA = input().split()
NA.sort()
M = int(input())
NB = input().split()
for b in NB:
    result = bin(NA, b, 0, N-1)
    if result != None:
        print(1)
    else:
        print(0)