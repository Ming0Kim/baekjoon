import sys
input = sys.stdin.readline

n = int(input())
nlst = list(map(int, input().split()))
nlst.sort()
m = int(input())
mlst = list(map(int, input().split()))

def bin(num):
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if nlst[mid] == num:
            return 1
        elif nlst[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in mlst:
    print(bin(i), end=' ')