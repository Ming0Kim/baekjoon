def solution(common):
    answer = flag = 0
    N = len(common)
    dif = common[0] - common[1]
    for i in range(N-1):
        if common[i] - common[i+1] != dif:
            flag = 1
    if flag:
        answer = common[-1]*(common[-1]//common[-2])
    else: 
        answer = common[-1]-dif
    return answer