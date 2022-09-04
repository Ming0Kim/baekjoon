# 함수
def chk(arr, val):
    arr.sort(reverse=True)

    new = []
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if i != j and j != k and k != i:
                    sm = arr[i] + arr[j] + arr[k]
                    new.append(sm)
    new.sort(reverse=True)
    for i in new:
        if i <= val:
            return i

N, M = map(int, input().split())
lst = list(map(int, input().split()))
print(chk(lst, M))