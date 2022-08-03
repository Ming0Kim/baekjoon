N = int(input())

for _ in range(N):

    OX = input()
    score = 0
    sum_s = 0
    for ox in OX:
        if ox == 'O':
            score += 1
            sum_s += score
        else :
            score = 0
    print(sum_s)