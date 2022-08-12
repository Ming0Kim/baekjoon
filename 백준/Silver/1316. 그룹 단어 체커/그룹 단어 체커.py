# 입력
cnt = 0
N = int(input())
for _ in range(N):
    word = input()

    # lst 에 그룹 단어 알파벳 어펜드
    lst = [word[0]]
    for i in word:
        if lst[-1] != i:
            lst.append(i)
    
    # set(lst)를 통한 중복 완벽 제거
    # set의 len 과 lst의 len 비교
    
    if len(set(lst)) == len(lst):
        cnt +=1
print(cnt)