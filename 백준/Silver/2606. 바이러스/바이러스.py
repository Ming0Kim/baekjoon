# dfs 함수
def dfs(start):
    global cnt
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
# 입력
com = int(input())
arr = [[]*(com+1) for _ in range(com+1)]
pair = int(input())
for _ in range(pair):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)
# visited 초기화
visited = [0]*(com+1)
cnt = 0
dfs(1)   # 컴퓨터 1부터 시작
# 출력
print(cnt)