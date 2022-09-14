# 입력
N = int(input())

sm = 0                # 산술평균
lst = []              # 중앙값
dic = {}              # 최빈값
mx, mn = -4000, 4000  # 범위

for _ in range(N):
    num = int(input())
    sm += num         # 산술평균
    lst.append(num)   # 중앙값

    if num in dic:    # 최빈값
       dic[num] += 1
    else:
        dic[num] = 1

    if num > mx:      # 범위
        mx = num
    if num < mn:
        mn = num
print(int(round(sm/N,0)))          # 산술평균
lst.sort()
print(lst[N//2])      # 중앙값
value = max(dic.values())
freq = [k for k, v in dic.items() if v == value]
freq.sort()
if len(freq) == 1:
    print(freq[0])
else:
    print(freq[1])
# print(freq)
print(mx-mn)
