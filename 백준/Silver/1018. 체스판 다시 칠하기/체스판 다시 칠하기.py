# 입력
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# print(arr)

mn = 64   # 다를 수 있는 요소의 갯수 최댓값: 64로 설정

# 새로운 arr 만들어서 8X8 부분 출력
for row in range(N-8+1):
    for col in range(M-8+1):
        # 출력한 newarr의 시작점을 A에 할당
        A = 'W'
        # 'B'일 상정했을 때 틀린 것은 wrongb에 저장
        wronga = 0  # 틀린 갯수 세기 용
        wrongb = 0  # 틀린 갯수 세기 용
        for r in range(8):
            for c in range(8):

                if r%2==0:
                    if c%2==0:
                        # 짝수행 짝수열은 A와 같아야함
                        if arr[row+r][col+c] != A:
                            wronga +=1
                        else:
                            wrongb +=1
                    else:
                        # 짝수행 홀수열은 A와 달라야함
                        if arr[row+r][col+c] == A:
                            wronga +=1
                        else:
                            wrongb +=1
                else:
                    if c%2 == 0:
                        # 홀수행 짝수열은 A와 달라야함
                        if arr[row+r][col+c] == A:
                            wronga +=1
                        else:
                            wrongb +=1
                    else:
                        # 홀수행 홀수열은 A와 같아야함
                        if arr[row+r][col+c] != A:
                            wronga +=1
                        else:
                            wrongb +=1

        if wronga < mn:
            mn = wronga
        if wrongb < mn:
            mn = wrongb


print(mn)
